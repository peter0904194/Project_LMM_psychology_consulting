from Multi_Modal.analysis.gpt_vision_analysis import analyze_with_gpt4
from Multi_Modal.analysis.yolo_analysis import analyze_with_yolo
from Multi_Modal.analysis.question_analysis import get_questionnaire_responses

def main():
    # 설정
    image_path = "Multi_Modal/ex/test_image1.jpg"  # 분석할 이미지 경로
    api_key = "api_key"
    print("🚀 멀티모달 이미지 분석을 시작합니다...")

    # 1. GPT-4 Vision 분석 및 이미지 유형 판단
    print("\n1️⃣ GPT-4 Vision 이미지 분석 중...")
    gpt4_json_path, yolo_model, questionnaire_path, suffix, img_num = analyze_with_gpt4(image_path, api_key)
    if gpt4_json_path:
        print(f"✅ GPT-4 Vision 분석 완료: {gpt4_json_path}")
        print(f"✅ 선택된 YOLO 모델: {yolo_model}")
        print(f"✅ 선택된 설문지: {questionnaire_path}")

        # 2. YOLO 분석
        print("\n2️⃣ YOLO 객체 감지 분석 중...")
        yolo_json_path, yolo_img_path = analyze_with_yolo(image_path, yolo_model, suffix, img_num)
        print(f"✅ YOLO 분석 완료: {yolo_json_path}")
        print(f"✅ 탐지 결과 이미지 저장: {yolo_img_path}")

        # 3. 설문지 응답
        print("\n3️⃣ 설문지 응답 수집 중...")
        questionnaire_path = get_questionnaire_responses(questionnaire_path, suffix, img_num)
    else:
        print("❌ GPT-4 Vision 분석 실패")

    print("\n✨ 모든 분석이 완료되었습니다!")

if __name__ == "__main__":
    main()
