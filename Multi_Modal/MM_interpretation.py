import json
import os
import openai

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    # 분석할 유형/번호 입력
    suffix = input("분석 유형을 입력하세요 (나무: t, 집: h, 사람: p): ").strip().lower()
    img_num = input("분석할 그림 번호를 입력하세요 (예: 1): ").strip()

    # 파일 경로 설정
    gpt4_path = f"Multi_Modal/analysis_result/gpt4_analysis_{suffix}{img_num}.json"
    yolo_path = f"Multi_Modal/analysis_result/yolo_analysis_{suffix}{img_num}.json"
    question_path = f"Multi_Modal/analysis_result/question_answers_{suffix}{img_num}.json"

    # 프롬프트 경로 설정
    if suffix == 't':
        prompt_path = "Multi_Modal/prompt/interpret_prompt_t.txt"
    elif suffix == 'h':
        prompt_path = "Multi_Modal/prompt/interpret_prompt_h.txt"
    elif suffix == 'p':
        prompt_path = "Multi_Modal/prompt/interpret_prompt_p.txt"
    else:
        print("지원하지 않는 유형입니다.")
        return

    # 데이터 불러오기
    gpt4_analysis = load_json(gpt4_path)
    yolo_analysis = load_json(yolo_path)
    question_answers = load_json(question_path)
    with open(prompt_path, 'r', encoding='utf-8') as f:
        interpret_prompt = f.read()

    # API 키 입력
    # api_key = input("OpenAI API 키를 입력하세요: ").strip()
    api_key = "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"
    client = openai.OpenAI(api_key=api_key)

    # 프롬프트에 데이터 삽입
    prompt = interpret_prompt.format(
        gpt4_analysis=json.dumps(gpt4_analysis, ensure_ascii=False, indent=2),
        yolo_analysis=json.dumps(yolo_analysis, ensure_ascii=False, indent=2),
        question_answers=json.dumps(question_answers, ensure_ascii=False, indent=2),
        json_data=""
    )

    print("\n📝 GPT-4o에게 최종 해석 요청 중...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )
    result = response.choices[0].message.content

    # 결과 출력 및 저장
    print("\n===== 최종 통합 해석 결과 =====\n")
    print(result)
    output_path = f"Multi_Modal/analysis_result/final_interpret_{suffix}{img_num}.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"\n✅ 최종 해석 결과가 저장되었습니다: {output_path}")

if __name__ == "__main__":
    main()
