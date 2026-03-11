# ai_engine/risk_engine.py

import joblib
import os


MODEL_PATH = "models/risk_model.pkl"


def compute_risk_score(cpu=0, memory=0, network=0):

    score = (cpu * 0.5) + (memory * 0.3) + (network * 0.2)

    return min(score / 100, 1)


def classify_risk(score):

    if score < 0.2:
        return "SAFE"

    if score < 0.5:
        return "MEDIUM"

    return "DANGEROUS"


def predict_execution(risk_score):

    if not os.path.exists(MODEL_PATH):
        return risk_score < 0.2

    model = joblib.load(MODEL_PATH)

    return model.predict([[risk_score]])[0]