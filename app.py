from flask import Flask, render_template, request
import joblib
import pandas as pd
from textblob import TextBlob
from collections import Counter
import re

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# In-memory storage (or later use CSV/database)
review_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = None
    prediction_class = None
    chart_data = {"real": 0, "fake": 0}
    sentiment_data = {"positive": 0, "neutral": 0, "negative": 0}
    word_freq = {}

    if request.method == "POST":
        review = request.form["review"]
        
        # Predict
        vector = vectorizer.transform([review])
        prediction = model.predict(vector)[0]

        prediction_text = "Fake Review" if prediction == 1 else "Real Review"
        prediction_class = "fake" if prediction == 1 else "real"

        # Save to history
        review_history.append({"review": review, "prediction": prediction})

        # Update counts
        chart_data["real"] = sum(1 for r in review_history if r["prediction"] == 0)
        chart_data["fake"] = sum(1 for r in review_history if r["prediction"] == 1)

        # Sentiment analysis
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            sentiment_data["positive"] += 1
        elif polarity < -0.1:
            sentiment_data["negative"] += 1
        else:
            sentiment_data["neutral"] += 1

        # Word Frequency
        words = re.findall(r'\b\w+\b', review.lower())
        common = Counter(words).most_common(5)
        word_freq = dict(common)

    return render_template("index.html",
                           prediction_text=prediction_text,
                           prediction_class=prediction_class,
                           chart_data=chart_data,
                           sentiment_data=sentiment_data,
                           word_freq=word_freq)

if __name__ == "__main__":
    app.run(debug=True)
