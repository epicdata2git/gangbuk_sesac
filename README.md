# 🌸 SSAC\_TALK - 새싹 대화 친구 봇

잔잔한 자연 배경과 감성적인 말풍선 스타일의 UI를 갖춘 Streamlit 기반의 대화 챗봇입니다.
Upstage의 Solar LLM(`ChatUpstage`)을 사용하여 정감 있고 부드러운 말투로 응답합니다.

---

## 📌 주요 특징

* 자연/꽃무늬 배경과 감성적인 채팅 UI (CSS 포함)
* LangChain 기반 LLM 메모리 대화 지원
* Upstage Solar 모델 사용 (`langchain-upstage`)
* 정제된 말투 필터링 (반복 제거, 문장 간소화)

---

## 🛠️ 실행 방법

1. Python 가상환경 활성화 및 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

2. `.env` 파일 생성 (Upstage API 키 입력)

```env
UPSTAGE_API_KEY=sk-xxxxxxxxxxxxxxxx
```

3. Streamlit 앱 실행

```bash
streamlit run app.py
```

---

## 📄 파일 구성

| 파일명                | 설명                         |
| ------------------ | -------------------------- |
| `app.py`           | 메인 Streamlit 챗봇 앱 코드       |
| `Utils.py`         | 대화 초기화 및 출력용 유틸 함수         |
| `requirements.txt` | 필요한 Python 패키지 목록          |
| `.env`             | API 키 설정용 파일 (배포 시 제외해야 함) |

---

## 💬 사용 예시

```text
질문: 내일 날씨 어때?
답변: 제가 정확히 알 수는 없지만, 날씨 예보를 확인해보시면 좋을 것 같아요! 🌤️
```

---

## 🧩 사용된 기술

* Streamlit UI
* LangChain + RunnableWithMessageHistory
* Upstage solar-1-mini-chat
* Redis (선택적 사용)

---

## ⚠️ 주의사항

* `requirements.txt`에는 PyPI에서 설치 가능한 패키지만 포함해야 합니다.
* `langchain-upstage`는 PyPI 등록된 최신 버전 사용 권장
* `redis`는 Streamlit Cloud 배포 시 제외하세요.

---

## ✨ 만든 이유

자연스럽고 감성적인 대화를 나누는
“친구 같은 AI 챗봇”을 직접 구현하고자 시작했습니다 🌿
