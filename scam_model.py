import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Sample training data
data = {
    "message": [
        "Free entry in 2 a wkly comp to win FA Cup",
        "Hey, how are you doing?",
        "Congratulations! You have won a prize",
        "Let's meet at 5 PM today",
        "Urgent! Your account will be suspended",
    ],
    "label": [1, 0, 1, 0, 1]  # 1 = scam, 0 = safe
}

df = pd.DataFrame(data)

# 2. Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]

# 3. Train
model = MultinomialNB()
model.fit(X, y)

# 4. Save model and vectorizer in current directory
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)


# 🧪 Optional: Inference function
def is_scam_message(text):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    features = vectorizer.transform([text])
    prediction = model.predict(features)
    return int(prediction[0])
