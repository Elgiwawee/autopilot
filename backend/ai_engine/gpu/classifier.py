# ai_engine/gpu/classifier.py

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)

def train_gpu_model(X, y):
    model.fit(X, y)


# Feature:  p95 utilization, variance, time of day, replica count



def gpu_action_decision(prediction, p95):
    if prediction == "OVERPROVISIONED" and p95 < 40:
        return "downgrade_gpu"
    return "no_action"
