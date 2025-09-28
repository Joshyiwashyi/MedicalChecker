import os
import joblib

# Paths
BASE_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
ML_DIR = os.path.join(PROJECT_ROOT, "ml")

disease_model = joblib.load(os.path.join(ML_DIR, "disease_model.pkl"))
medicine_model = joblib.load(os.path.join(ML_DIR, "medicine_model.pkl"))
advice_model   = joblib.load(os.path.join(ML_DIR, "advice_model.pkl"))
vectorizer     = joblib.load(os.path.join(ML_DIR, "vectorizer.pkl"))

def predict_all(text):
    X_vec = vectorizer.transform([text])

    disease  = disease_model.predict(X_vec)[0]
    medicine = medicine_model.predict(X_vec)[0]
    advice   = advice_model.predict(X_vec)[0]

    return {
        "disease": disease,
        "medicine": medicine,
        "advice": advice
    }
