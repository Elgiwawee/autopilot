# ai_engine/spot/model.py

from sklearn.ensemble import GradientBoostingClassifier
import joblib

model = GradientBoostingClassifier()

def train(X, y):
    model.fit(X, y)
    joblib.dump(model, "spot_model.pkl")


def allow_spot(probability):
    return probability < 0.05  # 5% risk threshold
