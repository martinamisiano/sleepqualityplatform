import joblib
import pandas as pd
import matplotlib.pyplot as plt

MODEL_PATH = "backend/model/model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def preprocess(data):
    return pd.DataFrame([data])

def predict(data):
    model = load_model()
    df = preprocess(data)
    pred = model.predict(df)[0]
    return {"sleep_quality": str(pred)}

def plot_user_data(data):
    df = pd.DataFrame([data])
    df.T.plot(kind="bar")
    plt.savefig("plot.png")
    return {"msg":"plot saved"}
