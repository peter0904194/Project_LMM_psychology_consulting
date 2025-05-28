#HTP(집-나무-사람) 그림 기반 AI 멀티모달 심리 평가 시스템
본 프로젝트는 심리검사 도구인 HTP(집-나무-사람) 그림을 AI 기반으로 분석하는 멀티모달 시스템을 구축한 것이다. 먼저 YOLOv8을 활용해 그림에서 수관, 줄기, 뿌리 등 주요 요소를 객체 탐지하고, 각 객체의 위치, 크기, 비율 등의 구조적 정보를 JSON 형태로 정제하였다. 이어서 GPT-4를 통해 해당 JSON 정보, 그림의 전체적 형태에 대한 묘사, 사용자의 응답(예: 그린 이유, 감정 등)을 종합적으로 활용하여 심리적 해석을 생성하였다. 이 과정은 시각적 요소와 언어적 요소, 사용자의 주관적 진술을 통합 분석함으로써 보다 정교하고 개인화된 심리 상담 결과를 도출하는 데 목적이 있다.

<img width="865" alt="image" src="https://github.com/user-attachments/assets/4fe7cd39-4e23-41e1-982c-1f9ea70657c5" />
<img width="870" alt="image" src="https://github.com/user-attachments/assets/8e943e03-631e-43bc-8637-32924944c5b1" />
<img width="868" alt="image" src="https://github.com/user-attachments/assets/250ca955-68f3-408d-87af-987cbffaa97f" />
<img width="867" alt="image" src="https://github.com/user-attachments/assets/ac1a38b9-ac2e-4f2d-b161-abbb0b7bbc66" />
<img width="865" alt="image" src="https://github.com/user-attachments/assets/94c8a65c-7f01-4cba-9021-fbe7fa6bd92b" />
<img width="863" alt="image" src="https://github.com/user-attachments/assets/dc994409-a298-4574-a5e4-4a87355a339c" />

