import json
import os
import re
from ultralytics import YOLO

def analyze_with_yolo(image_path, model_path, suffix, img_num):
    """YOLO를 사용한 객체 감지 분석"""
    model = YOLO(model_path)
    results = model(image_path)

    image_width = results[0].orig_shape[1]
    image_height = results[0].orig_shape[0]

    objects = []
    summary = {}

    for box in results[0].boxes:
        cls = int(box.cls[0])
        class_name = model.names[cls]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = [round(float(v), 2) for v in box.xyxy[0].tolist()]
        width = round(x2 - x1, 2)
        height = round(y2 - y1, 2)
        area = round(width * height, 2)
        area_ratio = round(area / (image_width * image_height) * 100, 2)

        obj_info = {
            "class": class_name,
            "class_id": cls,
            "confidence": round(conf, 2),
            "bbox": {
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "width": width, "height": height,
                "area": area, "area_ratio": area_ratio
            }
        }
        objects.append(obj_info)

        if class_name not in summary:
            summary[class_name] = {"count": 0, "total_area_ratio": 0.0}
        summary[class_name]["count"] += 1
        summary[class_name]["total_area_ratio"] += area_ratio

    for v in summary.values():
        v["total_area_ratio"] = round(v["total_area_ratio"], 2)

    result_json = {
        "image": image_path,
        "width": image_width,
        "height": image_height,
        "summary": summary,
        "objects": objects
    }

    os.makedirs('Multi_Modal/analysis_result', exist_ok=True)
    yolo_output_path = f'Multi_Modal/analysis_result/yolo_analysis{suffix}{img_num}.json'
    with open(yolo_output_path, 'w', encoding='utf-8') as f:
        json.dump(result_json, f, ensure_ascii=False, indent=4)

    # 탐지 결과 이미지 저장
    output_img_path = f'Multi_Modal/analysis_result/detected_image{suffix}{img_num}.jpg'
    results[0].save(filename=output_img_path)

    return yolo_output_path, output_img_path 