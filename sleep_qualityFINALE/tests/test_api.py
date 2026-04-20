import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.main import app

client = TestClient(app)

def test_prediction_endpoint_valid():
    response = client.post("/v1/predict", json={
        "age": 30,
        "stress_level": 5,
        "physical_activity": 3,
        "bmi": 24
    })
    assert response.status_code == 200
    data = response.json()
    assert "sleep_quality" in data
    assert "confidence" in data
    assert 0 <= data["confidence"] <= 1

def test_prediction_endpoint_invalid_age():
    response = client.post("/v1/predict", json={
        "age": -5,
        "stress_level": 5,
        "physical_activity": 3,
        "bmi": 24
    })
    assert response.status_code == 422

def test_prediction_endpoint_missing_field():
    response = client.post("/v1/predict", json={
        "age": 30,
        "stress_level": 5,
        "bmi": 24
    })
    assert response.status_code == 422

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Sleep Quality Predictor" in response.json()["message"]

from unittest.mock import patch  # Aggiungi all'inizio del file con gli altri import

def test_prediction_with_mock():
    """Test con mocking del servizio di predizione"""
    mock_result = {
        "sleep_quality": "Good",
        "confidence": 0.95,
        "top_factors": ["stress", "activity"],
        "suggestions": ["Test suggestion"],
        "probabilities": {"Poor": 0.05, "Good": 0.95}
    }
    
    with patch('backend.services.prediction_service.predict', return_value=mock_result):
        response = client.post("/v1/predict", json={
            "age": 30,
            "stress_level": 5,
            "physical_activity": 3,
            "bmi": 24
        })
        assert response.status_code == 200
        assert response.json()["sleep_quality"] == "Good"
        assert response.json()["confidence"] == 0.95
