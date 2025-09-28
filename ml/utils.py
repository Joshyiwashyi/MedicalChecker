import joblib

model = joblib.load("ml/model.pkl")
vectorizer = joblib.load("ml/vectorizer.pkl")

def predict_condition(user_input: str):
    X = vectorizer.transform([user_input])
    return model.predict(X)[0]
