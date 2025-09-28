import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = pd.read_csv("database/medical_question_answer_dataset_50000.csv")

# Features (input symptoms/questions)
X = data["Symptoms/Question"]

# Labels (outputs)
y_disease = data["Disease Prediction"]
y_medicine = data["Recommended Medicines"]
y_advice = data["Advice"]

# Convert text → numerical features (TF-IDF)
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2))  
X_vec = vectorizer.fit_transform(X)

# Train Logistic Regression models
disease_model = LogisticRegression(max_iter=500)
disease_model.fit(X_vec, y_disease)

medicine_model = LogisticRegression(max_iter=500)
medicine_model.fit(X_vec, y_medicine)

advice_model = LogisticRegression(max_iter=500)
advice_model.fit(X_vec, y_advice)

# Save models + vectorizer
joblib.dump(disease_model, "ml/disease_model.pkl")
joblib.dump(medicine_model, "ml/medicine_model.pkl")
joblib.dump(advice_model, "ml/advice_model.pkl")
joblib.dump(vectorizer, "ml/vectorizer.pkl")

print("✅ Logistic Regression models trained and saved successfully!")
