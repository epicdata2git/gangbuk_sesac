import streamlit as st
from Utils import init_conversation, print_conversation ,StreamHandler
from langchain_community.chat_message_histories import ChatMessageHistory, RedisChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import ChatMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_upstage import ChatUpstage
from dotenv import load_dotenv
import os

# 🌿 자연 배경 + 꽃방 규정
background_css = """
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1605296867304-46d5465a13f1?auto=format&fit=crop&w=1950&q=80');
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    color: #2e2e2e;
    font-family: 'Nanum Pen Script', cursive;
    display: flex;
    justify-content: center;
}
main.block-container {
    max-width: 800px;
    margin: auto;
    padding: 2rem;
    background-color: rgba(255, 255, 255, 0.92);
    border-radius: 25px;
    box-shadow: 0 0 20px rgba(180, 240, 180, 0.5);
    border: 5px double #c5e1a5;
    background-image: url('https://www.transparenttextures.com/patterns/floral-white.png');
    background-blend-mode: lighten;
}
div.stChatMessage {
    background-color: rgba(255, 255, 255, 0.96) !important;
    border: 3px solid #81c784;
    padding: 1.3rem !important;
    border-radius: 20px !important;
    margin-bottom: 1.5rem !important;
    background-image: url('https://www.transparenttextures.com/patterns/flower.png');
    background-blend-mode: lighten;
    font-size: 1.1rem;
    backdrop-filter: blur(2px);
    box-shadow: 0 0 12px rgba(140, 200, 140, 0.5);
}
</style>
"""
st.set_page_config(page_title="SSAC_TALK", page_icon="🍀")
background_css = """
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1505843513577-22bb7d21e455?auto=format&fit=crop&w=1950&q=80');
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    color: #2c2c2c;
    font-family: 'Nanum Myeongjo', serif;
    display: flex;
    justify-content: center;
}
main.block-container {
    max-width: 850px;
    margin: auto;
    padding: 2rem;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    box-shadow: 0 0 30px rgba(200, 180, 255, 0.5);
    border: 6px double #e1bee7;
    background-image: url('https://www.transparenttextures.com/patterns/garden.png');
    background-blend-mode: lighten;
}
div.stChatMessage {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid #ce93d8;
    padding: 1.2rem !important;
    border-radius: 16px !important;
    margin-bottom: 1.2rem !important;
    background-image: url('https://www.transparenttextures.com/patterns/flower.png');
    background-blend-mode: lighten;
    font-size: 1.1rem;
    backdrop-filter: blur(2px);
    box-shadow: 0 0 12px rgba(180, 120, 220, 0.5);
}
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)
st.markdown(background_css, unsafe_allow_html=True)
st.title("🌸✨💎🍀 새싹봇 🍀💎✨🌸")
st.caption("당신의 이야기를 들어주는 잔잔한 대화 친구입니다 🌿")

load_dotenv()
REDIS_URL = "redis://localhost:6379/0"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "RunnableWithMessageHistory"

if "store" not in st.session_state:
    st.session_state["store"] = dict()

def get_reids_message_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(session_id, url=REDIS_URL)

with st.sidebar:
    session_id = st.text_input("세션 ID 적어보지~", value="ssac0724")
    clear_space = st.button("지난 기록 삭제할까요?")
    if clear_space:
        st.session_state["messages"] = []
        st.rerun()

init_conversation()
print_conversation()

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state["store"]:
        st.session_state["store"][session_id] = ChatMessageHistory()
    return st.session_state["store"][session_id]

if user_input := st.chat_input("궁금증을 풀어드립니다"):
    st.chat_message("user").write(user_input)
    st.session_state["messages"].append(ChatMessage(role="user", content=user_input))

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatUpstage(
            streaming=True,
            callbacks=[stream_handler],
            model='solar-1-mini-chat'
        )

        prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        '''
        너는 친절하고 차분한 대화 친구야. 사용자가 하는 질문이나 고민에 대해 너무 길지 않게 따뜻하고 명확하게 대답해줘.
        중복되거나 부자연스러운 말투는 피하고, 공감과 함께 자연스럽고 일관된 말투로 응답해줘.
        너무 정중하거나 딱딱하게 굴지 말고, 친구처럼 이야기하듯이 말해.
        '''
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

        runnable = prompt | llm

        chain_with_memory = RunnableWithMessageHistory(
            runnable=runnable,
            get_session_history=get_reids_message_history,
            input_messages_key="question",
            history_messages_key="history",
        )

        response = chain_with_memory.invoke(
            {"question": user_input},
            config={"configurable": {"session_id": session_id}},
        )

        response_text = response.content
        forbidden_phrases = [
            "아, 미안해요",
            "더 부드럽게 말해볼게요",
            "아, 더 정중하게 말해볼게요",
            "죄송해요",
            "추천드리고 싶어요",
            "도움이 되었으면 좋겠어요",
            "길게 설명해볼게요",
            "한번 더 말해볼게요",
            "한번 더 알려드릴게요"
        ]
        for phrase in forbidden_phrases:
                response_text = response_text.replace(phrase, "")

        cut_points = ["아, 미안해요", "아, 더 정중하게 말해볼게요"]
        for phrase in cut_points:
            if phrase in response_text:
                response_text = response_text.split(phrase)[0].strip()
                break

        if len(response_text) > 200:
            response_text = response_text[:200].rsplit('.', 1)[0].strip() + "."

        

        st.session_state["messages"].append(ChatMessage(role="assistant", content=response_text))