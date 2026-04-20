from backend.services.prediction_service import predict

def test_predict():
    res = predict({"age":25,"stress":5,"activity":3,"bmi":22})
    assert "sleep_quality" in res
    assert "top_factors" in res
