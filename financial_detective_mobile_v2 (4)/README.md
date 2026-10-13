# 🕵️ 금융사기 수사대

귀여운 탐정 테마의 **모바일 우선 금융사기 예방 학습 웹앱**입니다. 실제 사기 유형을 바탕으로 한 8문항 상황형 테스트, 즉시 해설, 탐정 등급과 사건별 복습 기능을 제공합니다.

## 파일
- `app.py`: Streamlit 화면/상태/점수 기능
- `questions.py`: 8개 사건과 안전 대응 해설
- `assets/`: 탐정 일러스트 및 결과 배지(SVG)
- `.streamlit/config.toml`: 앱 테마
- `requirements.txt`: 배포용 패키지

## 실행
```bash
pip install -r requirements.txt
streamlit run app.py
```

## GitHub + Streamlit Community Cloud 배포
1. GitHub에서 **Public** 저장소 생성
2. 압축을 풀고 `app.py`, `questions.py`, `requirements.txt`, `README.md`, `assets` 폴더, `.streamlit` 폴더를 **저장소 최상위 폴더**에 업로드
3. https://share.streamlit.io 에서 새 앱 만들기
4. Repository: `<내 아이디>/<저장소 이름>` / Branch: `main` / Main file path: `app.py`
5. Deploy 후 8문항과 결과를 테스트하고 URL을 Slack에 공유

> 교육용 시뮬레이션이며 실제 금융사기의 확정 진단 또는 특정 기관의 공식 안내가 아닙니다. 개인정보를 입력받지 않습니다.
