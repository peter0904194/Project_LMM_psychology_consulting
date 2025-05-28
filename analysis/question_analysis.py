import json
import os

def get_questionnaire_responses(questionnaire_path, suffix, img_num):
    """설문지 응답 수집"""
    with open(questionnaire_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print("\n📋 설문지에 답변을 입력하세요:")
    for i, item in enumerate(questions, 1):
        print(f"{i}. {item['질문']}")
        answer = input("▶ 답변: ")
        item["응답"] = answer.strip()

    answer_path = f"Multi_Modal/analysis_result/question_answers{suffix}{img_num}.json"
    os.makedirs(os.path.dirname(answer_path), exist_ok=True)
    with open(answer_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"\n✅ 설문 응답 저장 완료: {answer_path}")
    return answer_path 