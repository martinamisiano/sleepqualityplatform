# Sleep Quality Platform 

## Features
- ML prediction
- Explainability (top factors)
- FastAPI backend
- Frontend UI
- Logging
- Docker ready

## Run
uvicorn backend.main:app --reload

## Docker
docker build -t sleep-app .
docker run -p 8000:8000 sleep-app
