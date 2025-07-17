import json
import random
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open('intents.json', encoding='utf-8') as f:
    data = json.load(f)

sentences = []
labels = []

# Use 'tag' instead of 'intent'
for item in data['intents']:
    for pattern in item['patterns']:
        sentences.append(pattern)
        labels.append(item['tag'])

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = LogisticRegression()
model.fit(X, labels)

def predict_intent(text):
    text_vector = vectorizer.transform([text])
    return model.predict(text_vector)[0]

def get_response(intent, language="English"):
    for item in data['intents']:
        if item['tag'] == intent:
            return item['responses'].get(language, item['responses']['English'])

    # Fallback default response
    return {
        "English": "Sorry, I didn't understand that.",
        "Hindi": "माफ कीजिए, मैं समझ नहीं पाई।",
        "Gujarati": "માફ કરશો, હું સમજી શક્યો નહીં."
    }.get(language, "Sorry, I didn't understand that.")
