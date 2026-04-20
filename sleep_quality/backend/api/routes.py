from fastapi import APIRouter
from backend.services.prediction_service import predict, plot_user_data

router = APIRouter()

@router.post("/predict")
def predict_sleep(data: dict):
    return predict(data)

@router.post("/plot")
def plot(data: dict):
    return plot_user_data(data)
