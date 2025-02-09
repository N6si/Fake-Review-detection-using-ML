import pandas as pd
import numpy as np
import joblib
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download NLTK stopwords
nltk.download('stopwords')

# Load dataset (Ensure dataset has "review" and "label" columns)
df = pd.read_csv("fake_reviews_dataset.csv")

# Fix label column: Convert 'CG' → 1 (Fake), 'OR' → 0 (Real)
df['label'] = df['label'].map({'CG': 1, 'OR': 0})

# Remove missing values
df.dropna(subset=['review', 'label'], inplace=True)

# Preprocess text (remove stopwords)
stop_words = set(stopwords.words('english'))
df['cleaned_review'] = df['review'].apply(lambda x: ' '.join(
    [word for word in x.split() if word.lower() not in stop_words]
))

# Convert text to numerical format using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)  # Convert text to numbers
X = vectorizer.fit_transform(df['cleaned_review'])  # Features
y = df['label']  # Target (1 = Fake, 0 = Real)

# Split dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model using Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Check model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Save trained model and vectorizer
joblib.dump(model, "fake_review_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model and vectorizer saved successfully!")
