import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import joblib
import json
import os

# Crea directory model se non esiste
os.makedirs('backend/model', exist_ok=True)

# Carica dati
df = pd.read_csv('ml/sleep_dataset.csv')
print(f"Dataset caricato: {df.shape}")

X = df[['age', 'stress_level', 'physical_activity', 'bmi']]
y = df['sleep_quality']

target_map = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Excellent': 3}
y_encoded = y.map(target_map)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [10, 20, None],
    'classifier__min_samples_split': [2, 5],
}

grid_search = GridSearchCV(
    pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1
)

print("\nAddestramento in corso...")
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print(f"\nMigliori parametri: {grid_search.best_params_}")
print(f"Miglior accuracy CV: {grid_search.best_score_:.3f}")

y_pred = best_model.predict(X_test)

print("\n" + "="*50)
print("CLASSIFICATION REPORT")
print("="*50)
print(classification_report(y_test, y_pred, target_names=list(target_map.keys())))

rf_model = best_model.named_steps['classifier']
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nFEATURE IMPORTANCE:")
print(feature_importance)

feature_importance.to_json('backend/model/feature_importance.json', orient='records')

joblib.dump(best_model, 'backend/model/model.pkl')
print("\n✅ Modello salvato in 'backend/model/model.pkl'")

metadata = {
    'model_type': str(type(rf_model).__name__),
    'features': list(X.columns),
    'classes': list(target_map.keys()),
    'class_map': target_map,
    'accuracy': float(grid_search.best_score_),
    'test_accuracy': float((y_pred == y_test).mean()),
    'n_samples': len(df),
    'n_features': len(X.columns)
}

with open('backend/model/metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print("\n📊 METADATI:")
for k, v in metadata.items():
    print(f"  {k}: {v}")
