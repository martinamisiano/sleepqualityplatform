from fastapi import APIRouter
from backend.services.prediction_service import predict
from backend.core.schemas import UserInput

router = APIRouter()

@router.post("/predict")
def predict_sleep(data: UserInput):
    return predict(data.dict())
