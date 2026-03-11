# ai_engine/gpu/infer.py

import joblib

model = joblib.load("gpu_model.pkl")

def gpu_decision(features, p95):
    prediction = model.predict([features])[0]

    if prediction == 0 and p95 < 40:
        return "DOWNGRADE_GPU"

    return "NO_ACTION"
