import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import os

# Load data
df = pd.read_csv("phishing_emails.csv")

# Text vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train classifier
model = MultinomialNB()
model.fit(X, y)

# Predict on the same data (just for demo)
predictions = model.predict(X)

# Save results
df["prediction"] = predictions
os.makedirs("results", exist_ok=True)
df.to_csv("results/phishing_predictions.csv", index=False)

# Output
print("=== Classification Report ===")
print(classification_report(y, predictions))

