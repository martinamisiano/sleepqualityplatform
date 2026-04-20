import joblib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

MODEL_PATH = "backend/model/model.pkl"
FEATURES = ["age","stress","activity","bmi"]

def load_model():
    return joblib.load(MODEL_PATH)

def preprocess(data):
    return pd.DataFrame([data])[FEATURES]

import numpy as np

def predict(data):
    model = load_model()
    df = preprocess(data)

    prediction = model.predict(df)[0]

    #  probabilità (confidence)
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df)[0]
        confidence = float(np.max(proba))
    else:
        confidence = None

    #  explainability (feature importance)
    importances = model.feature_importances_
    feature_names = df.columns

    feature_importance = dict(zip(feature_names, importances))

    # top 2 fattori
    top_factors = sorted(
        feature_importance,
        key=feature_importance.get,
        reverse=True
    )[:2]

    #  suggerimento semplice
    suggestions_map = {
        "stress": "Try reducing stress before bedtime",
        "activity": "Increase physical activity during the day",
        "bmi": "Maintain a healthy BMI",
        "age": "Maintain consistent sleep habits"
    }

    suggestions = [suggestions_map.get(f, "") for f in top_factors]

    return {
        "sleep_quality": str(prediction),
        "confidence": confidence,
        "top_factors": top_factors,
        "suggestions": suggestions
    }
