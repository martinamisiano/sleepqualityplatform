from fastapi import APIRouter, HTTPException, Depends
from backend.core.schemas import UserInput, PredictionResponse
from backend.services.prediction_service import predict
import time
from collections import defaultdict
from datetime import datetime, timedelta
from fastapi import Request
from fastapi import APIRouter, HTTPException, Depends, Request

router = APIRouter(prefix="/v1", tags=["predictions"])

# Rate limiting semplice
rate_limits = defaultdict(list)

def rate_limit_check(client_ip: str, max_requests: int = 10, window_seconds: int = 60):
    now = datetime.now()
    rate_limits[client_ip] = [
        req_time for req_time in rate_limits[client_ip]
        if now - req_time < timedelta(seconds=window_seconds)
    ]
    
    if len(rate_limits[client_ip]) >= max_requests:
        raise HTTPException(status_code=429, detail="Too many requests")
    
    rate_limits[client_ip].append(now)

@router.post("/predict", response_model=PredictionResponse)
async def predict_sleep(data: UserInput, request: Request):
    # Estrae l'IP reale del client
    client_ip = request.client.host
    if client_ip is None:
        client_ip = "unknown"
        
    try:
        rate_limit_check(client_ip)
        result = predict(data.dict())
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@router.get("/model/info")
async def model_info():
    from backend.services.prediction_service import get_predictor
    predictor = get_predictor()
    return predictor.metadata
