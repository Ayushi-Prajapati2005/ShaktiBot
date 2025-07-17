# # Home.py
# import streamlit as st

# st.set_page_config(page_title="ShaktiBot 🌸", page_icon="🌸", layout="centered")

# st.title("🌸 Welcome to ShaktiBot")
# st.markdown("""
# Welcome to **ShaktiBot**, your AI companion for guidance, support, and empowerment.  
# 👧 Ask about career, education, rights, health, and more.  
# 🗣 Talk or type in **English**, **Hindi**, or **Gujarati**.  

# 👉 Go to the **Chat** page from the sidebar to start chatting with ShaktiBot!
# """)
import streamlit as st

st.set_page_config(page_title="ShaktiBot 🌸", page_icon="🌸", layout="centered")

# ---- Custom CSS Styling ----
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #ffffff, #f0f0f0);
        font-family: 'Segoe UI', sans-serif;
        padding: 2rem;
    }
    .title {
        text-align: center;
        font-size: 3em;
        color: #C71585;
        margin-bottom: 0.5em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.5em;
        color: #333;
        margin-bottom: 2em;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 2em;
    }
    .stButton > button {
        background-color: #C71585;
        color: white;
        font-size: 1.2em;
        padding: 0.7em 2em;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #a50e6d;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ---- Page Content ----
st.markdown("<div class='title'>🌸 Welcome to ShaktiBot</div>", unsafe_allow_html=True)
st.markdown("""
<div class='subtitle'>
Empowering Women & Girls through AI 💬<br>
Ask about education, safety, rights, mental health, career, and more.
</div>
""", unsafe_allow_html=True)


# Button to navigate to Chat page
if st.button("💬 Start Chatting with ShaktiBot"):
    st.switch_page("chat")
