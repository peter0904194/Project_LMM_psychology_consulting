import openai
import base64
import json
import re
import os

def analyze_with_gpt4(image_path, api_key):
    """GPT-4 Vision을 사용한 이미지 분석"""
    client = openai.OpenAI(api_key=api_key)

    # 이미지 base64 인코딩
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    # 1. 이미지 분류
    classification_prompt = "이 이미지는 나무 그림인가요, 집 그림인가요, 사람 그림인가요? '나무', '집', '사람', '기타' 중 하나로만 답하세요."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": classification_prompt},
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]}
        ]
    )
    classification = response.choices[0].message.content.strip()

    # 2. 프롬프트 선택 및 접미사 결정
    img_base = os.path.splitext(os.path.basename(image_path))[0]
    match = re.search(r'\d+', img_base)
    img_num = match.group() if match else "1"

    if "나무" in classification:
        prompt_path = "Multi_Modal/prompt/vision_prompt_t.txt"
        yolo_model = "Multi_Modal/best_t.pt"
        questionnaire_path = "Multi_Modal/question/question_t.json"
        suffix = "_t"
    elif "집" in classification:
        prompt_path = "Multi_Modal/prompt/vision_prompt_h.txt"
        yolo_model = "Multi_Modal/best_h.pt"
        questionnaire_path = "Multi_Modal/question/question_h.json"
        suffix = "_h"
    elif "사람" in classification:
        prompt_path = "Multi_Modal/prompt/vision_prompt_p.txt"
        yolo_model = "Multi_Modal/best_p.pt"
        questionnaire_path = "Multi_Modal/question/question_p.json"
        suffix = "_p"
    else:
        print("지원하지 않는 그림 유형입니다.")
        return None, None, None, None, None

    with open(prompt_path, "r", encoding="utf-8") as f:
        vision_prompt = f.read()

    # 3. 상세 분석
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": vision_prompt},
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                {"type": "text", "text": "이미지의 시각적 특징을 분석해 주세요. 결과는 한국어로 JSON 형식으로 작성해 주세요."}
            ]}
        ]
    )

    # 4. 결과 저장
    result_raw = response.choices[0].message.content
    json_match = re.search(r"\{[\s\S]*\}", result_raw)

    if json_match:
        try:
            result_clean = json.loads(json_match.group())
            output_path = f"Multi_Modal/analysis_result/gpt4_analysis{suffix}{img_num}.json"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result_clean, f, ensure_ascii=False, indent=2)
            return output_path, yolo_model, questionnaire_path, suffix, img_num
        except json.JSONDecodeError as e:
            print("❌ JSON 파싱 실패:", e)
            return None, None, None, None, None
    return None, None, None, None, None 