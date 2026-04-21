#  Sleep Quality Predictor

## Key Results
- Achieved ~84% accuracy in sleep quality classification
- Identified stress level as the most impactful factor (42%)
- Built an end-to-end pipeline from data generation to API deployment

  ## Data Analysis Highlights
- Performed feature engineering on lifestyle variables
- Analyzed relationships between stress, activity, and sleep quality
- Interpreted model outputs to generate actionable suggestions

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

An **end-to-end machine learning platform** that predicts sleep quality based on lifestyle factors (age, stress, physical activity, BMI). Built with production-ready practices: modular architecture, comprehensive testing, containerization, and API versioning.

>  **Educational Purpose Only** – Not intended for medical use or clinical decisions.

---

##  Problem Statement

Sleep tracking devices generate raw data, but interpreting this data into meaningful insights requires structured analysis. This system bridges the gap by providing:
- **Real-time predictions** based on lifestyle factors
- **Explainable AI** (feature importance & personalized suggestions)
- **Production-ready API** for integration with health applications

---

##  Key Features

| Feature | Implementation |
|---------|----------------|
|  **ML Pipeline** | RandomForest with GridSearchCV optimization |
|  **Explainability** | Feature importance + personalized suggestions |
|  **API** | FastAPI with auto-docs, validation, rate limiting |
|  **Testing** | Unit + integration tests (pytest) |
|  **Containerization** | Docker-ready with multi-stage build |
|  **Monitoring** | Health checks + model metadata endpoints |
|  **Versioning** | API versioning (`/v1/predict`) |

---

##  Architecture
┌─────────────┐ ┌──────────────┐ ┌─────────────────┐
│ Frontend │────▶│ FastAPI │────▶│ ML Model │
│ (HTML/JS) │ │ (v1 API) │ │ (RandomForest) │
└─────────────┘ └──────────────┘ └─────────────────┘
│ │
▼ ▼
┌──────────────┐ ┌─────────────────┐
│ Rate Limiting│ │ Feature Import. │
│ Validation │ │ Metadata Store │
└──────────────┘ └─────────────────┘


### Project Structure
sleepqualityplatform/
├── backend/ # FastAPI application
│ ├── api/ # Route handlers
│ ├── core/ # Pydantic schemas
│ ├── services/ # Business logic & ML
│ └── model/ # Serialized model + metadata
├── ml/ # ML pipeline
│ ├── generate_dataset.py # Synthetic data generation
│ └── train_professional.py # Training + optimization
├── tests/ # Unit & integration tests
├── frontend/ # Simple UI
├── Dockerfile # Container configuration
├── Makefile # Automation commands
└── requirements.txt # Dependencies


---

##  Quick Start

### Local Development

```bash
# 1. Clone repository
git clone https://github.com/martinamisiano/sleepqualityplatform.git
cd sleepqualityplatform

# 2. Setup environment
make setup          # Installs dependencies & generates dataset

# 3. Train model
make train          # Trains RandomForest with hyperparameter tuning

# 4. Run tests
make test           # Executes test suite

# 5. Start API server
make run            # Starts FastAPI on http://localhost:8000


Docker Deployment

# Build image
make docker-build

# Run container
make docker-run

# Access API at http://localhost:8000

API Documentation
Once running, visit http://localhost:8000/docs for interactive Swagger documentation.
Method	Endpoint	Description
POST	/v1/predict	Predict sleep quality
GET	/health	Health check
GET	/model/info	Model metadata
GET	/	API information

Predict Endpoint Example
curl -X POST http://localhost:8000/v1/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "stress_level": 5,
    "physical_activity": 3,
    "bmi": 24
  }'

Response:
{
  "sleep_quality": "Good",
  "confidence": 0.82,
  "top_factors": ["stress", "activity"],
  "suggestions": [
    " Practice mindfulness or meditation before bed",
    " Increase daily physical activity (aim for 30min/day)"
  ],
  "probabilities": {
    "Poor": 0.05,
    "Fair": 0.13,
    "Good": 0.82,
    "Excellent": 0.00
  }
}

Model Details
Dataset

Size: 1,000 synthetic samples
Features: Age, stress level, physical activity, BMI
Target: Sleep quality (Poor, Fair, Good, Excellent)
Distribution: Balanced across classes

Training Process
- Algorithm: RandomForestClassifier
- Hyperparameter tuning: GridSearchCV (5-fold cross-validation)
- Preprocessing: StandardScaler
- Train/Test split: 80/20 with stratification

Performance Metrics

Class	Precision	Recall	F1-Score
Poor	0.85	0.82	0.83
Fair	0.81	0.79	0.80
Good	0.84	0.86	0.85
Excellent	0.88	0.87	0.87

Overall Accuracy: ~84% (cross-validated)
Feature Importance

Stress Level (0.42)
Physical Activity (0.31)
BMI (0.18)
Age (0.09)


Testing Strategy
make test


Monitoring & Observability
Endpoint	Purpose
/health	Liveness probe for orchestration
/model/info	Model version, accuracy, feature importance
Logging	Python logging module with INFO level
Rate Limiting	10 requests per 60 seconds per client


Deployment
# Optional customizations (future releases)
API_PORT=8000
MAX_REQUESTS_PER_MINUTE=10
LOG_LEVEL=INFO



Cloud Deployment Ready

Container Registry: Docker Hub / GitHub Container Registry
Orchestration: Kubernetes (via Deployment + Service)
CI/CD: GitHub Actions template included below
<details> <summary><b>GitHub Actions CI/CD Template</b></summary>

name: CI/CD Pipeline
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with: { python-version: '3.9' }
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Generate dataset & train model
        run: |
          python ml/generate_dataset.py
          python ml/train_professional.py
      - name: Run tests
        run: pytest tests/ -v
  docker:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build Docker image
        run: docker build -t sleep-quality-app .



Development Commands
Command	Description
make setup	Install dependencies & generate dataset
make train	Train and optimize the model
make test	Run test suite
make run	Start development server
make docker-build	Build Docker image
make docker-run	Run Docker container
make clean	Remove cache files


License

This project is for educational purposes only. Not intended for clinical or medical use. The author assumes no liability for misuse.

 Author

Martina Misiano

 Performance Benchmarks

Metric	Value
API Response Time (p95)	~50ms
Model Inference Time	~15ms
Throughput (requests/sec)	~200 (local)
Memory Usage	~150MB
Container Size	~500MB
