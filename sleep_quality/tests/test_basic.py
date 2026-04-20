from backend.services.prediction_service import predict

def test_predict():
    assert "sleep_quality" in predict({"age":25,"stress":5,"activity":3,"bmi":22})
