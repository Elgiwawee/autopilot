# billing/baseline/engine.py

from statistics import mean
from billing.baseline.strategies import (
    rolling_average,
    weekday_average,
)


class BaselineEngine:

    def compute(self, *, cloud_account, service, resource_id, target_date):
        candidates = []

        r1 = rolling_average(resource_id, service, cloud_account, target_date)
        if r1:
            candidates.append(("rolling_21d", r1, 0.6))

        r2 = weekday_average(resource_id, service, cloud_account, target_date)
        if r2:
            candidates.append(("weekday", r2, 0.4))

        if not candidates:
            return None, 0.0, []

        baseline = mean(v for _, v, _ in candidates)

        confidence = sum(weight for _, _, weight in candidates)
        confidence = min(confidence, 1.0)

        explanations = [
            f"{name}: {value:.4f}" for name, value, _ in candidates
        ]

        return baseline, confidence, explanations
