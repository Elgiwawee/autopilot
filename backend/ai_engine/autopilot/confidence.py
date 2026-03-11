# ai_engine/autopilot/confidence.py

def confidence_score(success_rate: float) -> float:
    """
    Executive-facing trust metric.
    """
    return round(success_rate * 100, 1)
