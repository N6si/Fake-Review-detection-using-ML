# Fake-Review-detection-using-ML

📌 Overview
Fake reviews are a growing problem in eCommerce and online platforms, misleading customers and damaging trust. This project aims to detect fake reviews using Machine Learning (ML) by analyzing text patterns, sentiment, and other linguistic features. The model classifies reviews as genuine or fake based on trained data, helping platforms ensure review authenticity.

![Image](https://github.com/user-attachments/assets/11762483-fa66-41e7-9763-6200cee21941)
![Image](https://github.com/user-attachments/assets/ee89b5df-5771-48d2-b7e1-bd43946711b8)

📂 Dataset
Uses a publicly available dataset or a custom dataset of labeled fake and real reviews.

🏗️ Installation & Usage

Step 1.Clone the repository
git clone https://github.com/N6si/Fake-Review-detection-using-ML
cd Fake-Review-detection

Step 2: Setup Environment
You need the following:

Python (3.8+)
Libraries: pandas, sklearn, nltk, Flask
Node.js (for React UI)
To install dependencies, run:

You need to run the installation command in the terminal (command prompt). Here’s how:

For Windows:
Open Command Prompt (cmd) or Windows PowerShell.
Navigate to your project folder using:
cd path\to\your\project   //run in cmd 

pip install pandas numpy scikit-learn nltk flask   //run in cmd

Step 3:We will train a machine learning model to detect whether a review is real or fake.
We need a dataset with real and fake reviews.
You can download a dataset from Kaggle (e.g., Amazon or Yelp fake review dataset).
The dataset should have two columns:
review (The text of the review)
label (1 = Fake, 0 = Real)

--already given the fake review detection dataset it is in excel saved in .csv file with 40k reviews

train_model.py
This file contains the script for for training the fake review detection model.

After saving, open Command Prompt and run:
Navigate to your project folder:
python train_model.py //in cmd

This will train the model and save two files:

fake_review_model.pkl – The trained model
vectorizer.pkl – The text vectorizer

after running the model it will give 88% accuracy 

 step 4: Create test_model.py to Predict Fake/Real Review

 Create a new file test_model.py and add this code:

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


python test_model.py   // in cmd

---And thn add UI using Flask












