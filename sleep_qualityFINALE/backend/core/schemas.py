from pydantic import BaseModel

class UserInput(BaseModel):
    age: int
    stress: float
    activity: float
    bmi: float
