def compute_risk_score(
    env_risk,
    cpu_variance,
    network_risk,
    dependency_risk,
    age_risk
):
    return (
        env_risk * 0.30 +
        cpu_variance * 0.25 +
        network_risk * 0.20 +
        dependency_risk * 0.15 +
        age_risk * 0.10
    )


def classify_risk(risk_score):
    if risk_score < 0.25:
        return "SAFE"
    elif risk_score < 0.6:
        return "REVIEW"
    return "BLOCKED"
