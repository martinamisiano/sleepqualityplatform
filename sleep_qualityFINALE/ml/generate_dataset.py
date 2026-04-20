import pandas as pd
import numpy as np

np.random.seed(42)

n_samples = 1000

# Genera feature realistiche
age = np.random.normal(35, 12, n_samples).clip(18, 80).astype(int)
stress = np.random.uniform(1, 10, n_samples).round(1)
activity = np.random.uniform(0, 10, n_samples).round(1)
bmi = np.random.normal(26, 5, n_samples).clip(15, 45).round(1)

def calculate_sleep_quality(age, stress, activity, bmi):
    score = 70
    
    score -= stress * 3
    score += activity * 2
    
    if bmi < 18.5 or bmi > 30:
        score -= 15
    elif bmi > 25:
        score -= 5
    
    if age > 60:
        score += 5
    elif age < 25:
        score -= 3
    
    score += np.random.normal(0, 5)
    
    if score >= 75:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 45:
        return "Fair"
    else:
        return "Poor"

targets = [calculate_sleep_quality(a, s, act, b) 
           for a, s, act, b in zip(age, stress, activity, bmi)]

df = pd.DataFrame({
    'age': age,
    'stress_level': stress,
    'physical_activity': activity,
    'bmi': bmi,
    'sleep_quality': targets
})

df.to_csv('ml/sleep_dataset.csv', index=False)
print(f"Dataset creato: {len(df)} campioni")
print("\nDistribuzione classi:")
print(df['sleep_quality'].value_counts())
print("\nPrime 5 righe:")
print(df.head())