# 이미지 분석 설정
IMAGE_PATH = "Multi_Modal/ex/test_image1.jpg"  # 분석할 이미지 경로
API_KEY = "api_key"
# 결과 저장 경로
ANALYSIS_RESULT_DIR = "Multi_Modal/analysis_result"

# 모델 경로
YOLO_MODELS = {
    "tree": "Multi_Modal/best_t.pt",
    "house": "Multi_Modal/best_h.pt",
    "person": "Multi_Modal/best_p.pt"
}

# 프롬프트 파일 경로
PROMPT_FILES = {
    "tree": "Multi_Modal/prompt/vision_prompt_t.txt",
    "house": "Multi_Modal/prompt/vision_prompt_h.txt",
    "person": "Multi_Modal/prompt/vision_prompt_p.txt"
}

# 설문지 파일 경로
QUESTIONNAIRE_FILES = {
    "tree": "Multi_Modal/question/question_t.json",
    "house": "Multi_Modal/question/question_h.json",
    "person": "Multi_Modal/question/question_p.json"
} 