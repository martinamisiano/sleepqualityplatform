from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

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
    return {
        "message": "Sleep Quality Predictor API",
        "version": "2.0.0",
        "docs": "/docs",
        "health": "/health"
    }
