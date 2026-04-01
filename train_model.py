import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("synthetic_phishing_dataset_50k.csv")

X = data["text"]
y = data["label"]

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save model & vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved successfully")
