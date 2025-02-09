import joblib

# Load the saved model and vectorizer
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_review(review):
    transformed_review = vectorizer.transform([review])  # Convert text to numbers
    prediction = model.predict(transformed_review)  # Predict
    return "Fake Review" if prediction[0] == 1 else "Real Review"

# Test the model
while True:
    review = input("\nEnter a review to check (or type 'exit' to quit): ")
    if review.lower() == 'exit':
        break
    result = predict_review(review)
    print(f"Prediction: {result}")
