
# 🌸 ShaktiBot – AI Empowerment Chatbot for Women & Girls

**ShaktiBot** is an AI-powered, multilingual chatbot designed to empower women and girls by providing accessible, anonymous guidance on topics like mental health, legal rights, safety, education, and career development.

Built with **Python** and **Streamlit**, ShaktiBot supports both **text and voice input**, and responds in **English, Hindi, or Gujarati**.

---

## ✨ Features
- ✅ AI-based intent recognition using logistic regression
- 🗣️ Voice and text input support (Google Speech Recognition)
- 🌐 Multilingual responses (English, Hindi, Gujarati)
- 💬 Feedback logging system to improve responses
- 🎨 Clean, responsive Streamlit UI
- 📂 Modular code structure with future admin panel support

---

## 📁 Project Structure
```
ShaktiBot_Advanced/
├── Home.py                  # Landing page with intro & navigation
├──| pages
    |  Chat.py                  # Main chatbot interface
├── classifier.py            # Intent classification logic
├── intents.json             # Predefined intents and responses
├── responses_hi.json        # Hindi response mappings
├── responses_gu.json        # Gujarati response mappings
├── feedback_log.txt         # Feedback log from users
├── requirements.txt         # Required Python packages
└── assets/
    └── shaktibot_logo.png   # Optional logo image
```

---

## 🚀 How to Run
1. **Clone the repo:**
```bash
git clone https://github.com/your-username/ShaktiBot.git
cd ShaktiBot_Advanced
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
streamlit run Home.py
```

---

## 🔐 Privacy & Safety
- No login or personal data required.
- All chats are anonymous and stored only for feedback improvement.
- Local development does not collect any external data unless integrated.

---

## 📜 License
This project is licensed under the **MIT License**. See `LICENSE` file for more info.


---

## 📣 Acknowledgements
- Built using [Streamlit](https://streamlit.io)
- Voice input via [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- Inspired by UN Sustainable Development Goal 5: *Gender Equality*
