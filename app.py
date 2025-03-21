from flask import Flask, render_template, request
import joblib

model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = None
    prediction_class = None

    if request.method == "POST":
        review = request.form["review"]
        transformed_review = vectorizer.transform([review])
        pred = model.predict(transformed_review)

        if pred[0] == 1:
            prediction_text = "Fake Review 😡"
            prediction_class = "fake"
        else:
            prediction_text = "Real Review 😊"
            prediction_class = "real"

    return render_template("index.html", prediction_text=prediction_text, prediction_class=prediction_class)

if __name__ == "__main__":
    app.run(debug=True)

