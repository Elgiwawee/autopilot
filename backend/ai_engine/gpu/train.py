# ai_engine/gpu/train.py

from sklearn.ensemble import RandomForestClassifier
import joblib

model = RandomForestClassifier(n_estimators=100, random_state=42)

def train(X, y):
    model.fit(X, y)
    joblib.dump(model, "gpu_model.pkl")
