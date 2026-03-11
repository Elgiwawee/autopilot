
# ai_engine/ml/risk_model.py

import os
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import SGDClassifier


MODEL_PATH = "models/risk_model.pkl"


class RiskAnomalyModel:

    def __init__(self):
        self.model = IsolationForest(
            contamination=0.05,
            random_state=42,
        )

    def train(self, feature_history):
        """
        Train anomaly detection model.
        """
        self.model.fit(feature_history)

    def score(self, features):
        """
        Return normalized anomaly risk score between 0 and 1.
        """
        raw = self.model.decision_function([features])[0]

        return max(0.0, min(1.0, 1 - raw))

    def save(self):
        """
        Persist trained model.
        """
        os.makedirs("models", exist_ok=True)

        joblib.dump(self.model, MODEL_PATH)

    def load(self):
        """
        Load trained model if available.
        """
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)

ONLINE_MODEL_PATH = "models/online_risk_model.pkl"


class OnlineRiskModel:
    """
    Incremental learning model that updates after each action.
    """

    def __init__(self):

        self.model = SGDClassifier(loss="log_loss")

        self.is_initialized = False

    def partial_train(self, features, label):

        X = np.array([features])
        y = np.array([label])

        if not self.is_initialized:
            self.model.partial_fit(X, y, classes=np.array([0, 1]))
            self.is_initialized = True
        else:
            self.model.partial_fit(X, y)

    def predict(self, features):

        if not self.is_initialized:
            return 1

        X = np.array([features])

        prediction = self.model.predict(X)[0]

        return prediction

    def save(self):

        os.makedirs("models", exist_ok=True)

        joblib.dump(self.model, ONLINE_MODEL_PATH)

    def load(self):

        if os.path.exists(ONLINE_MODEL_PATH):
            self.model = joblib.load(ONLINE_MODEL_PATH)
            self.is_initialized = True

def load_risk_model():
    """
    Helper used by decision engine.
    """
    if not os.path.exists(MODEL_PATH):
        return None

    model = RiskAnomalyModel()
    model.load()

    return model

def load_online_model():

    model = OnlineRiskModel()
    model.load()

    return model