# Sleep Quality Predictor

A lightweight **end-to-end ML platform** that predicts sleep quality based on lifestyle factors (age, stress, physical activity, BMI).  
The project demonstrates **modular backend architecture**, **model explainability**, and **API-first design** – concepts directly transferable to production systems.

> **Disclaimer:** This is an **educational proof-of-concept**, not a medical tool. The current model is trained on a small dataset for demonstration purposes.

---

## What It Does

- Accepts user input (age, stress level, activity level, BMI) via a **REST API** (FastAPI)
- Returns:
  - Predicted sleep quality (e.g., "Good" / "Poor")
  - Confidence score
  - Top 2 influencing factors (e.g., stress, activity)
  - Personalized suggestions
- Provides a **simple HTML/JavaScript frontend** to interact with the API

---

## Technical Highlights

| Area | Implementation |
|------|----------------|
| **API Framework** | FastAPI (async, auto-docs, Pydantic validation) |
| **ML Model** | RandomForestClassifier with feature importance |
| **Explainability** | Real-time extraction of top contributing features |
| **Testing** | Pytest (unit tests for prediction service) |
| **Logging** | Python `logging` module (configurable) |
| **CORS** | Enabled for local frontend integration |
| **Containerization** | Docker-ready (Dockerfile included) |

---

## Project Structure (Current)

sleepqualityplatform/
├── backend/
│ ├── main.py # FastAPI app entrypoint
│ ├── api/
│ │ └── routes.py # /predict endpoint
│ ├── core/
│ │ └── schemas.py # Pydantic models
│ ├── services/
│ │ └── prediction_service.py # Model loading & inference
│ └── model/
│ └── model.pkl # Serialized RandomForest
├── ml/
│ └── train.py # Model training script (⚠️ tiny dataset)
├── tests/
│ └── test_api.py # Basic unit tests
├── frontend/
│ └── index.html # Minimal test UI
├── requirements.txt
└── Dockerfile


---

##  Quick Start

```bash
# Clone the repository
git clone https://github.com/martinamisiano/sleepqualityplatform.git
cd sleepqualityplatform

# Install dependencies
pip install -r requirements.txt

# Start the backend
uvicorn backend.main:app --reload

# Open frontend (in another terminal or just double-click)
open frontend/index.html

The API will be available at http://localhost:8000
Interactive docs: http://localhost:8000/docs

## API Usage
Endpoint: POST /predict

Request body:
{
  "age": 30,
  "stress": 5.0,
  "activity": 3.0,
  "bmi": 24.0
}

Response:

{
  "sleep_quality": "Good",
  "confidence": 0.82,
  "top_factors": ["stress", "activity"],
  "suggestions": [
    "Try reducing stress before bedtime",
    "Increase physical activity during the day"
  ]
}

Docker

docker build -t sleep-app .
docker run -p 8000:8000 sleep-app

Limitation:
 Model trained on only 4 synthetic samples
 No cross-validation or hyperparameter tuning
 Tests don't validate output values
 Frontend URL hardcoded to localhost
 No persistence / user history

Planned Improvement
 Replace with real dataset (e.g., Sleep Health Kaggle – 400+ records)
 Add GridSearchCV and MLflow tracking
 Add edge-case tests (negative age, missing fields)
 Make configurable via environment variable
 Add SQLite database + user sessions

## Future Roadmap (if this were a real product)

Replace training script with proper EDA notebook
Add CI/CD (GitHub Actions for auto-testing)
Deploy to cloud (Render / Railway) with live demo link
Add model versioning (DVC or MLflow)
Implement A/B testing framework (simulated)

## What I Learned / Demonstrated

Separation of concerns (routing → service → model)
API contract validation with Pydantic
Feature importance for basic explainability
Containerization basics (Docker)
Importance of realistic datasets (this project revealed that)

Author
Martina Misiano

## License

Educational use only. Not for clinical/medical purposes.


