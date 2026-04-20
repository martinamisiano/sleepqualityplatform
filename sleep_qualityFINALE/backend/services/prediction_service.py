import joblib
import pandas as pd
import logging
import json
from pathlib import Path
from typing import Dict, Any
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SleepPredictor:
    def __init__(self):
        self.model = None
        self.feature_importance = None
        self.metadata = None
        self.features = ['age', 'stress_level', 'physical_activity', 'bmi']
        self.load_artifacts()
    
    def load_artifacts(self):
        try:
            model_path = Path(__file__).parent.parent / "model" / "model.pkl"
            self.model = joblib.load(model_path)
            logger.info(f"Model loaded from {model_path}")
            
            metadata_path = Path(__file__).parent.parent / "model" / "metadata.json"
            with open(metadata_path) as f:
                self.metadata = json.load(f)
            
            importance_path = Path(__file__).parent.parent / "model" / "feature_importance.json"
            with open(importance_path) as f:
                self.feature_importance = json.load(f)
            
            logger.info("Metadata and feature importance loaded")
        except Exception as e:
            logger.error(f"Error loading artifacts: {e}")
            raise
    
    def validate_input(self, data: Dict[str, Any]) -> tuple[bool, str]:
        required_fields = self.features
        
        for field in required_fields:
            if field not in data:
                return False, f"Missing field: {field}"
        
        if data['age'] < 0 or data['age'] > 120:
            return False, "Age must be between 0 and 120"
        
        if data['stress_level'] < 0 or data['stress_level'] > 10:
            return False, "Stress must be between 0 and 10"
        
        if data['physical_activity'] < 0 or data['physical_activity'] > 24:
            return False, "Physical activity must be between 0 and 24 hours"
        
        if data['bmi'] < 10 or data['bmi'] > 50:
            return False, "BMI must be between 10 and 50"
        
        return True, "OK"
    
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        is_valid, error_msg = self.validate_input(data)
        if not is_valid:
            raise ValueError(error_msg)
        
        df = pd.DataFrame([data])[self.features]
        prediction_encoded = self.model.predict(df)[0]
        prediction_proba = self.model.predict_proba(df)[0]
        
        class_map = self.metadata['class_map']
        reverse_map = {v: k for k, v in class_map.items()}
        predicted_class = reverse_map[prediction_encoded]
        confidence = float(np.max(prediction_proba))
        
        # Suggerimenti personalizzati
        suggestions_map = {
            'stress': "🧘 Practice mindfulness or meditation before bed",
            'activity': "🏃 Increase daily physical activity (aim for 30min/day)",
            'BMI': "🥗 Consult a nutritionist for a balanced diet plan",
            'age': "⏰ Maintain consistent sleep schedule"
        }
        
        # Determina fattori principali
        top_factors = []
        if data['stress_level'] > 7:
            top_factors.append('stress')
        if data['physical_activity'] < 3:
            top_factors.append('activity')
        if data['bmi'] > 25 or data['bmi'] < 18.5:
            top_factors.append('BMI')
        
        if not top_factors:
            top_factors = ['stress', 'activity']
        
        top_factors = top_factors[:2]
        suggestions = [suggestions_map.get(f, "Keep up good habits!") for f in top_factors]
        
        return {
            "sleep_quality": predicted_class,
            "confidence": round(confidence, 3),
            "top_factors": top_factors,
            "suggestions": suggestions,
            "probabilities": {
                k: round(float(v), 3) 
                for k, v in zip(self.metadata['classes'], prediction_proba)
            }
        }

_predictor = None

def get_predictor():
    global _predictor
    if _predictor is None:
        _predictor = SleepPredictor()
    return _predictor

def predict(data: Dict[str, Any]) -> Dict[str, Any]:
    predictor = get_predictor()
    return predictor.predict(data)
