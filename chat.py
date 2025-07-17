import streamlit as st

st.set_page_config(page_title="Chat with ShaktiBot", page_icon="💬", layout="wide")


from classifier import predict_intent, get_response
import speech_recognition as sr

st.set_page_config(page_title="ShaktiBot 🌸", page_icon="🌸", layout="wide")

# ---- Custom CSS Styling ----
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f5f7fa, #ffe6f0);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 3em;
        color: #C71585;
    }
    .msg-bubble {
        padding: 1rem;
        border-radius: 20px;
        margin: 10px;
        max-width: 80%;
        word-wrap: break-word;
    }
    .user {
        background: rgba(255, 204, 229, 0.8);
        align-self: flex-end;
        margin-left: auto;
    }
    .bot {
        background: rgba(204, 255, 255, 0.6);
        align-self: flex-start;
        margin-right: auto;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Title and Description ----
st.markdown("<div class='title'>🌸 ShaktiBot – Empowerment Chatbot for Women & Girls</div>", unsafe_allow_html=True)
st.markdown("##### 💬 Talk to me about career, rights, motivation, mental health, or anything on your mind.")

# ---- Language Selection ----
language = st.selectbox("🌐 Select Language", ["English", "Hindi", "Gujarati"])

# ---- Session State Initialization ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_input" not in st.session_state:
    st.session_state.last_input = ""
if "last_intent" not in st.session_state:
    st.session_state.last_intent = ""
if "last_response" not in st.session_state:
    st.session_state.last_response = ""

# ---- Voice Input ----
st.markdown("🎙️ **Optional:** Upload a voice question (.wav)")
audio_file = st.file_uploader("Upload Voice (WAV)", type=["wav"])
text_input = st.text_input("✍️ Type your message below:")

# ---- Handle Voice Input ----
if audio_file:
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        voice_input = recognizer.recognize_google(audio)
        st.success(f"🗣 You said: {voice_input}")
        text_input = voice_input
    except sr.UnknownValueError:
        st.error("❌ Could not understand the audio.")
    except sr.RequestError:
        st.error("❌ Could not connect to Google Speech Recognition service.")

# ---- Process New Input ----
if text_input and text_input != st.session_state.last_input:
    intent = predict_intent(text_input)
    response = get_response(intent, language) or "I'm not sure how to respond to that."
    
    # Save to session state
    st.session_state.chat_history.append({"role": "user", "text": text_input})
    st.session_state.chat_history.append({"role": "bot", "text": response})
    st.session_state.last_input = text_input
    st.session_state.last_intent = intent
    st.session_state.last_response = response

    # Log the input
    with open("feedback_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Input: {text_input} | Intent: {intent} | Response: {response}\n")

# ---- Display Chat ----
st.markdown("### 🧾 Conversation")
for msg in st.session_state.chat_history:
    style = "user" if msg["role"] == "user" else "bot"
    st.markdown(f"<div class='msg-bubble {style}'>{msg['text']}</div>", unsafe_allow_html=True)

# ---- Feedback Section ----
if st.session_state.last_response:
    st.markdown("#### Was the last response helpful?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Yes"):
            with open("feedback_log.txt", "a", encoding="utf-8") as f:
                f.write(f"[YES] {st.session_state.last_input} | Intent: {st.session_state.last_intent} | Response: {st.session_state.last_response}\n")
            st.success("Thanks for your feedback! 💖")

    with col2:
        if st.button("👎 No"):
            with open("feedback_log.txt", "a", encoding="utf-8") as f:
                f.write(f"[NO] {st.session_state.last_input} | Intent: {st.session_state.last_intent} | Response: {st.session_state.last_response}\n")
            st.info("Thanks! We'll use this to improve.")
