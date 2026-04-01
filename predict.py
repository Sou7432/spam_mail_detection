import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_text(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    probability = model.predict_proba(text_vec).max()

    if prediction == 1:
        return "Phishing 🚨", round(probability * 100, 2)
    else:
        return "Safe ✅", round(probability * 100, 2)
