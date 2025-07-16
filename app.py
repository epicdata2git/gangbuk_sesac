import streamlit as st

# 🌿 자연 배경 + 풀과 꽃 장식
st.set_page_config(page_title="욕쟁이 할매 봇", page_icon="🌸", layout="centered")

background_style = """
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    color: #222;
}

div.stChatMessage {
    background-color: rgba(255, 255, 255, 0.85) !important;
    padding: 1.3rem !important;
    border-radius: 20px !important;
    margin-bottom: 1.5rem !important;
    border: 3px solid #f48fb1; /* 연핑크 */
    box-shadow: 0 0 10px rgba(250, 160, 200, 0.7);
    background-image: url('https://www.transparenttextures.com/patterns/flowers.png');
    background-blend-mode: lighten;
    font-size: 1.1rem;
}
</style>
"""
st.markdown(background_style, unsafe_allow_html=True)

# 🍀 타이틀
st.title("🌼 욕쟁이 할매 봇 🌼")
st.markdown("**🌷 궁금한 거 있음 써봐~ 쪼금이라도 말 더듬으면 등짝 맞는다잉!! 🌿**")

# 📝 사용자 질문 받기
user_input = st.chat_input("뭐가 그리 궁금헌디? 어여 써봐라잉~")

# 💬 할매 응답 함수 (찐 할매 말투)
def halmae_reply(text):
    return (
        f"어휴~ '{text}' 요딴 걸 이제 물어봐? 이눔아~\n"
        f"내가 살아온 세월이 얼만디~ 그깟 건 말이제~\n"
        f"잘 들어~ 한 귀로 듣고 한 귀로 흘리면 등짝 맞아잉!! 👵🔥"
    )

# 🌼 출력
if user_input:
    st.chat_message("user").write(user_input)
    with st.chat_message("assistant"):
        st.markdown(halmae_reply(user_input))


