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

def predict(data):
    model = load_model()
    df = preprocess(data)

    pred = model.predict(df)[0]
    importances = model.feature_importances_

    # map feature importance
    feature_importance = dict(zip(FEATURES, importances))
    top = sorted(feature_importance, key=feature_importance.get, reverse=True)[:2]

    logging.info(f"Prediction: {pred}, Top factors: {top}")

    return {
        "sleep_quality": str(pred),
        "top_factors": top
    }
