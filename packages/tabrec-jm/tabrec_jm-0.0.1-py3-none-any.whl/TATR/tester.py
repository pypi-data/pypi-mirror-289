import cv2
import numpy as np
import json
import requests
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image
from matplotlib import pyplot as plt
import os
from collections import defaultdict
from pydantic_settings import BaseSettings
import torch
from fitz import Rect
import xml.etree.ElementTree as ET
import re

from TATR.slanet import TextTableMapping

from TATR.main import build_model_main
from TATR.util.slconfig import SLConfig
import TATR.postprocess as postprocess
import TATR.datasets.transforms as T


# REQUIREMENTS:
# pip install termcolor, pydantic_settings, addict, yapf, timm
# pip install -U openmim
# mim install mmengine
# mim install "mmcv>=2.0.0"
# mim install mmdet


def cells_to_html(cells):
    cells = sorted(cells, key=lambda k: min(k['column_nums']))
    cells = sorted(cells, key=lambda k: min(k['row_nums']))

    table = ET.Element("table")
    current_row = -1

    for cell in cells:
        this_row = min(cell['row_nums'])

        attrib = {}
        colspan = len(cell['column_nums'])
        if colspan > 1:
            attrib['colspan'] = str(colspan)
        rowspan = len(cell['row_nums'])
        if rowspan > 1:
            attrib['rowspan'] = str(rowspan)
        if this_row > current_row:
            current_row = this_row
            if cell['column header']:
                cell_tag = "th"
                row = ET.SubElement(table, "thead")
            else:
                cell_tag = "td"
                row = ET.SubElement(table, "tr")
        tcell = ET.SubElement(row, cell_tag, attrib=attrib)
        tcell.text = cell['cell text']

        html_content = ET.tostring(table, encoding="unicode", short_empty_elements=False)
        pattern = re.compile(r'</?[^>]+>')
        tags = pattern.findall(html_content)
    return tags


def get_class_map(data_type):
    if data_type == 'structure':
        class_map = {
            'no object': 0,
            'table row': 1,
            'table column': 2,
            'table spanning cell': 3
        }
    elif data_type == 'detection':
        class_map = {'table': 0, 'table rotated': 1, 'no object': 2}
    return class_map


str_class_name2idx = get_class_map('structure')
str_class_idx2name = {v: k for k, v in str_class_name2idx.items()}


def iob(bbox1, bbox2):
    """
    Compute the intersection area over box area, for bbox1.
    """
    intersection = Rect(bbox1).intersect(bbox2)

    bbox1_area = Rect(bbox1).get_area()
    if bbox1_area > 0:
        return intersection.get_area() / bbox1_area

    return 0


def refine_table_structure(table_structure, class_thresholds):
    """
    Apply operations to the detected table structure objects such as
    thresholding, NMS, and alignment.
    """
    rows = table_structure["rows"]
    columns = table_structure['columns']

    # Process spanning cells
    spanning_cells = [elem for elem in table_structure['spanning cells'] if not elem['projected row header']]
    projected_row_headers = [elem for elem in table_structure['spanning cells'] if elem['projected row header']]
    spanning_cells = postprocess.apply_threshold(spanning_cells, class_thresholds["table spanning cell"])
    # projected_row_headers = postprocess.apply_threshold(projected_row_headers,
    #                                                     class_thresholds["table projected row header"])
    spanning_cells += projected_row_headers
    # Align before NMS for spanning cells because alignment brings them into agreement
    # with rows and columns first; if spanning cells still overlap after this operation,
    # the threshold for NMS can basically be lowered to just above 0
    spanning_cells = postprocess.align_supercells(spanning_cells, rows, columns)
    spanning_cells = postprocess.nms_supercells(spanning_cells)

    postprocess.header_supercell_tree(spanning_cells)

    table_structure['columns'] = columns
    table_structure['rows'] = rows
    table_structure['spanning cells'] = spanning_cells
    # table_structure['column headers'] = column_headers

    return table_structure


def structure_to_cells(table_structure, tokens):
    """
    Assuming the row, column, spanning cell, and header bounding boxes have
    been refined into a set of consistent table structures, process these
    table structures into table cells. This is a universal representation
    format for the table, which can later be exported to Pandas or CSV formats.
    Classify the cells as header/access cells or data cells
    based on if they intersect with the header bounding box.
    """
    columns = table_structure['columns']
    rows = table_structure['rows']
    spanning_cells = table_structure['spanning cells']
    cells = []
    subcells = []

    # Identify complete cells and subcells
    # for column_num, column in enumerate(columns):
    for row_num, row in enumerate(rows):
        for column_num, column in enumerate(columns):
            column_rect = Rect(list(column['bbox']))
            row_rect = Rect(list(row['bbox']))
            cell_rect = row_rect.intersect(column_rect)
            header = 'column header' in row and row['column header']
            cell = {'bbox': list(cell_rect), 'row_nums': [row_num], 'column_nums': [column_num],
                    'column header': header}

            cell['subcell'] = False
            for spanning_cell in spanning_cells:
                spanning_cell_rect = Rect(list(spanning_cell['bbox']))
                if (spanning_cell_rect.intersect(cell_rect).get_area()
                    / cell_rect.get_area()) > 0.5:
                    cell['subcell'] = True
                    break

            if cell['subcell']:
                subcells.append(cell)
            else:
                # cell text = extract_text_inside_bbox(table_spans, cell['bbox'])
                # cell['cell text'] = cell text
                cell['projected row header'] = False
                cells.append(cell)

    for spanning_cell in spanning_cells:
        spanning_cell_rect = Rect(list(spanning_cell['bbox']))
        cell_columns = set()
        cell_rows = set()
        cell_rect = None
        header = True
        for subcell in subcells:
            subcell_rect = Rect(list(subcell['bbox']))
            subcell_rect_area = subcell_rect.get_area()
            if (subcell_rect.intersect(spanning_cell_rect).get_area()
                / subcell_rect_area) > 0.5:
                if cell_rect is None:
                    cell_rect = Rect(list(subcell['bbox']))
                else:
                    cell_rect.include_rect(Rect(list(subcell['bbox'])))
                cell_rows = cell_rows.union(set(subcell['row_nums']))
                cell_columns = cell_columns.union(set(subcell['column_nums']))
                # By convention here, all subcells must be classified
                # as header cells for a spanning cell to be classified as a header cell;
                # otherwise, this could lead to a non-rectangular header region
                header = header and 'column header' in subcell and subcell['column header']
        if len(cell_rows) > 0 and len(cell_columns) > 0:
            cell = {'bbox': list(cell_rect), 'row_nums': list(cell_rows), 'column_nums': list(cell_columns),
                    'column header': header, 'projected row header': spanning_cell['projected row header']}
            cells.append(cell)

    # Compute a confidence score based on how well the page tokens
    # slot into the cells reported by the model
    _, _, cell_match_scores = postprocess.slot_into_containers(cells, tokens)
    try:
        mean_match_score = sum(cell_match_scores) / len(cell_match_scores)
        min_match_score = min(cell_match_scores)
        confidence_score = (mean_match_score + min_match_score) / 2
    except:
        confidence_score = 0

    # Dilate rows and columns before final extraction
    # dilated_columns = fill_column_gaps(columns, table_bbox)
    dilated_columns = columns
    # dilated_rows = fill_row_gaps(rows, table_bbox)
    dilated_rows = rows
    for cell in cells:
        column_rect = Rect()
        for column_num in cell['column_nums']:
            column_rect.include_rect(list(dilated_columns[column_num]['bbox']))
        row_rect = Rect()
        for row_num in cell['row_nums']:
            row_rect.include_rect(list(dilated_rows[row_num]['bbox']))
        cell_rect = column_rect.intersect(row_rect)
        cell['bbox'] = list(cell_rect)

    span_nums_by_cell, _, _ = postprocess.slot_into_containers(cells, tokens, overlap_threshold=0.001,
                                                               unique_assignment=True, forced_assignment=False)

    for cell, cell_span_nums in zip(cells, span_nums_by_cell):
        cell_spans = [tokens[num] for num in cell_span_nums]
        # TODO: Refine how text is extracted; should be character-based, not span-based;
        # but need to associate
        cell['cell text'] = postprocess.extract_text_from_spans(cell_spans, remove_integer_superscripts=False)
        cell['spans'] = cell_spans

    # Adjust the row, column, and cell bounding boxes to reflect the extracted text
    num_rows = len(rows)
    rows = postprocess.sort_objects_top_to_bottom(rows)
    num_columns = len(columns)
    columns = postprocess.sort_objects_left_to_right(columns)
    min_y_values_by_row = defaultdict(list)
    max_y_values_by_row = defaultdict(list)
    min_x_values_by_column = defaultdict(list)
    max_x_values_by_column = defaultdict(list)
    for cell in cells:
        min_row = min(cell["row_nums"])
        max_row = max(cell["row_nums"])
        min_column = min(cell["column_nums"])
        max_column = max(cell["column_nums"])
        for span in cell['spans']:
            min_x_values_by_column[min_column].append(span['bbox'][0])
            min_y_values_by_row[min_row].append(span['bbox'][1])
            max_x_values_by_column[max_column].append(span['bbox'][2])
            max_y_values_by_row[max_row].append(span['bbox'][3])
    for row_num, row in enumerate(rows):
        if len(min_x_values_by_column[0]) > 0:
            row['bbox'][0] = min(min_x_values_by_column[0])
        if len(min_y_values_by_row[row_num]) > 0:
            row['bbox'][1] = min(min_y_values_by_row[row_num])
        if len(max_x_values_by_column[num_columns - 1]) > 0:
            row['bbox'][2] = max(max_x_values_by_column[num_columns - 1])
        if len(max_y_values_by_row[row_num]) > 0:
            row['bbox'][3] = max(max_y_values_by_row[row_num])
    for column_num, column in enumerate(columns):
        if len(min_x_values_by_column[column_num]) > 0:
            column['bbox'][0] = min(min_x_values_by_column[column_num])
        if len(min_y_values_by_row[0]) > 0:
            column['bbox'][1] = min(min_y_values_by_row[0])
        if len(max_x_values_by_column[column_num]) > 0:
            column['bbox'][2] = max(max_x_values_by_column[column_num])
        if len(max_y_values_by_row[num_rows - 1]) > 0:
            column['bbox'][3] = max(max_y_values_by_row[num_rows - 1])
    for cell in cells:
        row_rect = Rect()
        column_rect = Rect()
        for column_num in cell['column_nums']:
            column_rect.include_rect(list(columns[column_num]['bbox']))
        for row_num in cell['row_nums']:
            row_rect.include_rect(list(rows[row_num]['bbox']))
        cell_rect = column_rect.intersect(row_rect)
        if cell_rect.get_area() > 0:
            cell['bbox'] = list(cell_rect)
            pass

    cells = sorted(cells, key=lambda x: (min(x['row_nums']), min(x['column_nums'])))

    return cells, confidence_score


def objects_to_structures(objects, tokens, class_thresholds, bbox_size):
    """
    Process the bounding boxes produced by the table structure recognition model into
    a *consistent* set of table structures (rows, columns, spanning cells, headers).
    This entails resolving conflicts/overlaps, and ensuring the boxes meet certain alignment
    conditions (for example: rows should all have the same width, etc.).
    """

    # tables = [obj for obj in objects if obj['label'] == 'table']
    tables = []
    ss = {}
    ss['bbox'] = [0, 0, bbox_size[0], bbox_size[1]]
    tables.append(ss)

    table_structures = []

    for table in tables:
        table_objects = [obj for obj in objects if iob(obj['bbox'], table['bbox']) >= 0.5]
        table_tokens = [token for token in tokens if iob(token['bbox'], table['bbox']) >= 0.5]

        structure = {}

        columns = [obj for obj in table_objects if obj['label'] == 'table column']
        rows = [obj for obj in table_objects if obj['label'] == 'table row']
        # column_headers = [obj for obj in table_objects if obj['label'] == 'table column header']
        spanning_cells = [obj for obj in table_objects if obj['label'] == 'table spanning cell']
        for obj in spanning_cells:
            obj['projected row header'] = False
        projected_row_headers = [obj for obj in table_objects if obj['label'] == 'table projected row header']
        for obj in projected_row_headers:
            obj['projected row header'] = True
        spanning_cells += projected_row_headers
        # for obj in rows:
        #     obj['column header'] = False
        #     for header_obj in column_headers:
        #         if iob(obj['bbox'], header_obj['bbox']) >= 0.5:
        #             obj['column header'] = True

        # Refine table structures
        rows = postprocess.refine_rows(rows, table_tokens, class_thresholds['table row'])
        columns = postprocess.refine_columns(columns, table_tokens, class_thresholds['table column'])

        # Shrink table bbox to just the total height of the rows
        # and the total width of the columns
        row_rect = Rect()
        for obj in rows:
            row_rect.include_rect(obj['bbox'])
        column_rect = Rect()
        for obj in columns:
            column_rect.include_rect(obj['bbox'])
        table['row_column_bbox'] = [column_rect[0], row_rect[1], column_rect[2], row_rect[3]]
        table['bbox'] = table['row_column_bbox']

        # Process the rows and columns into a complete segmented table
        columns = postprocess.align_columns(columns, table['row_column_bbox'])
        rows = postprocess.align_rows(rows, table['row_column_bbox'])

        structure['rows'] = rows
        structure['columns'] = columns
        # structure['column headers'] = column_headers
        structure['spanning cells'] = spanning_cells

        if len(rows) > 0 and len(columns) > 1:
            structure = refine_table_structure(structure, class_thresholds)

        table_structures.append(structure)

    return table_structures


def box_cxcywh_to_xyxy(x):
    x_c, y_c, w, h = x.unbind(-1)
    b = [(x_c - 0.5 * w), (y_c - 0.5 * h), (x_c + 0.5 * w), (y_c + 0.5 * h)]
    return torch.stack(b, dim=1)


def rescale_bboxes(out_bbox, size):
    img_w, img_h = size
    b = box_cxcywh_to_xyxy(out_bbox)
    b = b * torch.tensor([img_w, img_h, img_w, img_h], dtype=torch.float32)
    return b


def outputs_to_objects(outputs, img_size, class_idx2name, threshold=0.5):
    m = outputs['pred_logits'].sigmoid().max(-1)
    # m = outputs['pred_logits'].softmax(-1).max(-1)
    pred_labels = list(m.indices.detach().cpu().numpy())[0]
    pred_scores = list(m.values.detach().cpu().numpy())[0]
    pred_bboxes = outputs['pred_boxes'].detach().cpu()[0]
    pred_bboxes = [elem.tolist() for elem in rescale_bboxes(pred_bboxes, img_size)]

    objects = []
    for label, score, bbox in zip(pred_labels, pred_scores, pred_bboxes):
        class_label = class_idx2name[int(label)]
        # if not class_label == 'no object':
        if class_label == 'table column' or class_label == 'table' or class_label == 'table row' or class_label == 'table spanning cell':
            objects.append({'label': class_label, 'score': float(score),
                            'bbox': [float(elem) for elem in bbox]})

    top_300_detections = sorted(objects, key=lambda x: x['score'], reverse=True)[:300]

    results = [detection for detection in top_300_detections if detection['score'] >= threshold]

    return results


def run_tatr(model, org_image, device):
    # transform images
    transform = T.Compose([
        T.RandomResize([(1024, 1024)], 1024),
        T.ToTensor(),
        # T.Normalize([0.449, 0.449, 0.449], [0.226, 0.226, 0.226])
        T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    thrs = 0.3
    str_class_thresholds = {
        "table column": thrs,
        "table row": thrs,
        "table spanning cell": 0.3
    }
    org_image = Image.fromarray(np.uint8(org_image)).convert('RGB')
    # org_image = torch.tensor(org_image)
    image, _ = transform(org_image, None)
    # predict images
    image_width, image_height = org_image.size
    out_formats = {}
    image = image[None].to(device)
    output = model(image)
    objects = outputs_to_objects(output, org_image.size, str_class_idx2name, thrs)
    tables_structure = objects_to_structures(objects, [], str_class_thresholds, org_image.size)
    tables_cells = [structure_to_cells(structure, [])[0] for structure in tables_structure]

    bbox_list = []
    for t in tables_cells[0]:
        bbox_list.append(t['bbox'])

    if any(not sublist for sublist in tables_cells):
        structure_list = ['<html>', '<body>', '<table>', '<tr>', '<td>', '</td>', '</tr>', '</table>', '</body>', '</html>']
        bbox_list = [[0, 0, image_width, image_height]]
    else:
        tables_htmls = [cells_to_html(cells) for cells in tables_cells]
        out_formats['html'] = tables_htmls
        structure_list = ['<html>', '<body>'] + out_formats['html'][0] + ['</body>', '</html>']

    return structure_list, bbox_list


class Settings(BaseSettings):
    character_dict_path: str
    weights_path: str
    classes_path: str
    tatr_weights_path: str
    tatr_config_path: str


# talbe 여러개 -> CROP::  for loop:: 구조인식

def ocrInference(image_file):
    pod_ip = os.getenv('POD_IP')
    print('POD_IP:', pod_ip)
    layout_url = f'http://{pod_ip}:8005/word_det/'

    # pil_image = Image.open(BytesIO(image_file))
    # pil_image = pil_image.convert('RGB')
    pil_image = Image.fromarray(np.uint8(image_file)).convert('RGB')

    # ###### not processing #####
    # np_image = np.array(pil_image)
    # bgr_image = np_image[:, :, ::-1]
    origin_w, origin_h = pil_image.size
    bytes_stream = BytesIO()
    pil_image.save(bytes_stream, format='JPEG')
    image_bytes = bytes_stream.getvalue()

    upload_file = ("tmp_img.png", image_bytes)

    detection_result_json = requests.post(layout_url, files={"file": upload_file})
    text_det_bboxes = json.loads(detection_result_json.json())['allbboxes']
    origin_text_det_bboxes = json.loads(detection_result_json.json())['origin-allbboxes']

    # 바운딩박스 크기 고려하여 중앙값 비교
    error_margin = 8
    sorted_boxes = sorted(text_det_bboxes,
                          key=lambda box: (
                              round((box[1] + box[3] / 2) / error_margin), box[0]))  # 상수는 관용 정도

    # resize_bboxes = []
    # ## recofg 위해서 이미지 사이즈 및 bbox 원복
    # resized_img_origin = image_resize(bgr_image, width=origin_w)
    # for bbox in sorted_boxes:
    #     ratio_bbox = resize_bbox(bbox, bgr_image.shape[1], origin_w)
    #     resize_bboxes.append(ratio_bbox)
    # print(f"resize {(new_img.shape[1])} to {(origin_w)}")
    # print(f"convert bbox {len(sorted_boxes)} to {len(resize_bboxes)}")

    # recog 위해서 이미지 한번 더 보냄
    # pil_image = Image.fromarray(resized_img_origin)
    # pil_image = pil_image.convert('RGB')

    # bytes_stream = BytesIO()
    # pil_image.save(bytes_stream, format='JPEG')
    # image_bytes = bytes_stream.getvalue()

    # upload_file = ("tmp_img.jpg", image_bytes)

    # detection_result_json = requests.post(layout_url, files={"file": upload_file})

    url = "http://61.82.130.19:38011/doc-recog/"  # 38004는 하나씩 받을 수 있음. bbox 뭉치 받기 위해선 38011
    url = f'http://{pod_ip}:8011/doc-recog/'

    data = {
        "img_name": "tmp_img.png",
        "bboxes": [text_det_bboxes]
    }

    tmp_rec_res = requests.post(url, data=json.dumps(data))
    tmp_rec_res = json.loads(tmp_rec_res.json())['data']

    text_list = tmp_rec_res[0]['rec_texts']
    text_result = []
    for idx, item in enumerate(text_list):
        rec_text = item.replace("<UKN>", "")
        text_result.append(rec_text)

    dt_boxes = origin_text_det_bboxes
    rec_res = text_result

    # 두 리스트를 zip으로 묶음
    zipped_boxes_texts = list(zip(dt_boxes, rec_res))

    # 정렬
    error_margin = 8
    sorted_zipped = sorted(zipped_boxes_texts, key=lambda item: (round((item[0][1] + item[0][3] / 2) / error_margin), item[0][0]))

    # 다시 풀어내기
    if sorted_zipped:
        sorted_text_det_bboxes, sorted_text_recognitions = zip(*sorted_zipped)
    else:
        sorted_text_det_bboxes, sorted_text_recognitions = [], []

    # 리스트로 변환
    sorted_text_det_bboxes = list(sorted_text_det_bboxes)
    sorted_text_recognitions = list(sorted_text_recognitions)

    xyxy_dt_boxes = []
    for idx, box_val in enumerate(sorted_text_det_bboxes):
        x, y, w, h = box_val
        xyxy_dt_boxes.append([x, y, x + w, y + h])

    return xyxy_dt_boxes, sorted_text_recognitions


with open('config.json', 'r', encoding='utf-8-sig') as f:
    config = json.load(f)
    settings = Settings(**config)

if __name__ == "__main__":
    table_rec_model_args = SLConfig.fromfile(settings.tatr_config_path)
    table_rec_model_args.device = torch.device('gpu')  # TODO: USE GPU
    table_rec_model, _, postprocessors = build_model_main(table_rec_model_args)
    checkpoint = torch.load(settings.tatr_weights_path, map_location='cpu')
    table_rec_model.load_state_dict(checkpoint['model'])
    _ = table_rec_model.eval()
    table_rec_model = table_rec_model.to(table_rec_model_args.device)

    cropped_img = cv2.imread('dummy-table.jpg')  # TODO: TabDetr Results:: Cropped images -> call run_tatr multiple-times.

    structure_list, bbox_list = run_tatr(model=table_rec_model, org_image=cropped_img, device=table_rec_model_args.device)
    print(structure_list, bbox_list)

    # TODO: OCR part.
    # dt_boxes, rec_res_origin = ocrInference(img)
    # rec_res = [(item, 1) for item in rec_res_origin]
    # text_table_mapper = TextTableMapping()
    # final_result = text_table_mapper(structure_list, bbox_list, dt_boxes, rec_res)
    # final_result += "<style>table {border-collapse: collapse;border: 1px solid black;width: 100%;}td {border: 1px solid black;padding: 8px;}tr {border: 1px solid black;}</style>"
    # print(final_result)
