from flask import Flask, render_template, request
import joblib

# Load the trained model and vectorizer
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        review = request.form["review"]
        transformed_review = vectorizer.transform([review])  # Convert text to numbers
        pred = model.predict(transformed_review)  # Predict
        prediction = "Fake Review 😡" if pred[0] == 1 else "Real Review 😊"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
