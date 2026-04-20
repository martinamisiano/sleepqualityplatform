from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

import logging
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Output su console
        # logging.FileHandler('app.log')  # Opzionale: salva su file
    ]
)

# Logger specifico per l'app
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sleep Quality Predictor API",
    description="AI-powered sleep quality prediction based on lifestyle factors",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def root():
    logger.info("Root endpoint chiamato")
    return {
        "message": "Sleep Quality Predictor API",
        "version": "2.0.0",
        "docs": "/docs",
        "health": "/health"
    }
