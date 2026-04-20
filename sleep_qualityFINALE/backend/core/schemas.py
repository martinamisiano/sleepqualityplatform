from pydantic import BaseModel, Field, validator
from typing import List, Dict

class UserInput(BaseModel):
    age: int = Field(..., ge=0, le=120, description="Age in years")
    stress_level: float = Field(..., ge=0, le=10, description="Stress level (0-10)")
    physical_activity: float = Field(..., ge=0, le=24, description="Hours of physical activity per day")
    bmi: float = Field(..., ge=10, le=50, description="Body Mass Index")
    
    @validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 120:
            raise ValueError('Age must be between 0 and 120')
        return v

class PredictionResponse(BaseModel):
    sleep_quality: str
    confidence: float
    top_factors: List[str]
    suggestions: List[str]
    probabilities: Dict[str, float]
