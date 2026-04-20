# Sleep Quality Platform 
# sleepqualityplatform
Sleep Quality Analyzer is a modular Python project that evaluates sleep quality based on biological criteria such as REM, deep sleep, wake time, and total duration. It includes a CLI interface, a separated core logic module, and automated tests to ensure correctness and maintainability.
Sleep quality is a critical factor in overall health and daily performance.
This project provides a platform that allows users to:
Input personal and lifestyle data
Predict sleep quality using a trained ML model
Receive insights about factors affecting sleep
The goal is to demonstrate how data-driven approaches can support personal health awareness.

# Sleep Quality Analyzer

A modular Python system that evaluates sleep quality based on physiological sleep-stage criteria (REM, deep, wake, total duration). The project is designed with clean architecture principles, testability-first design, and clear separation between business logic and interface layers.

## Problem statement

Sleep tracking devices generate raw sleep-stage data, but interpreting this data into meaningful sleep quality insights requires structured analysis.
This system transforms raw sleep session inputs into a standardized sleep quality classification, making the data interpretable and consistent.

## Overview

Sleep Quality Analyzer processes sleep session data and computes a quality score based on four biologically inspired rules:
Total sleep duration vs target
REM sleep percentage
Deep sleep percentage
Wake time percentage
Each sleep session is classified into one of:
SCADENTE
DISCRETA
BUONA
ECCELLENTE
The goal is to simulate a simplified but realistic sleep analysis engine similar to those used in health-tracking systems.

## Key features

Modular architecture (separation of concerns)
Rule-based scoring engine
Command-line interface (CLI)
Unit testing with pytest
Easily extensible core logic (ready for API or web integration)
Sleep quality prediction (ML model)
Input-based analysis (e.g. stress level, activity, BMI, etc.)
Modular backend structure
Model integration for real-time inference

## Architecture

The project is structured into two main components:
ML Pipeline
  Data preprocessing
  Model training
  Model serialization
Backend Application
  API endpoints
  Model loading and inference
  Request/response handling

## Installation

git clone https://github.com/martinamisiano/sleepqualityplatform.git
cd sleepqualityplatform
pip install -r requirements.txt

## Usage

python cli/main.py example_input.txt

## Input format

TARGET
wake rem deep light
wake rem deep light
...
 ## Output
 
The program produces:
Number of valid sleep sessions above target
Minimum, Maximum and Average total sleep duration
Quality classification for each session
Top 5 longest sleep sessions (sorted ascending)

## Architecture

The project is structured into two main components:
ML Pipeline
  Data preprocessing
  Model training
  Model serialization
Backend Application
  API endpoints
  Model loading and inference
  Request/response handling
  
## Tech Stack
Python
Machine Learning (scikit-learn / pandas / numpy)
Backend framework (Flask / FastAPI – adjust if needed)
Jupyter Notebook (for experimentation)

## Project Structure

sleep-quality-platform/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── services/
│   └── model/
│
├── ml/
│   ├── training.py
│   ├── preprocessing.py
│   └── dataset/
│
├── notebooks/
├── requirements.txt
└── README.md

## Installation

git clone https://github.com/martinamisiano/sleepqualityplatform.git
cd sleepqualityplatform
pip install -r requirements.txt
▶️ Run the application
python backend/app.py

## Example Input
{
  "age": 25,
  "stress_level": 7,
  "physical_activity": 3,
  "bmi": 22.5
}

## Example Output

{
  "sleep_quality": "Good"
}

The system provides:
- prediction
- confidence score
- key influencing factors
- personalized suggestions
  
## Model

The model is trained on a sleep health dataset and uses supervised learning to classify sleep quality.
Note: Performance may vary depending on dataset quality and generalization limits.

## Future Improvements
Add frontend dashboard
Improve model generalization
Add user history tracking
Deploy as a cloud service
##  Disclaimer
This project is for educational purposes only and is not intended for medical use.
##Author
Martina Misiano
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
