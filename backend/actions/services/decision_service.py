from actions.models import Decision

from ai_engine.risk_engine import (
    compute_risk_score,
    classify_risk,
)

from ai_engine.utilization import utilization_profile
from ai_engine.ml.predictor import predict_execution


def make_decision(plan):
    """
    Decide whether an action plan can be executed automatically.
    """

    resource = plan.resource

    # 1️⃣ Collect utilization metrics
    utilization = utilization_profile(resource)

    cpu = utilization.get("cpu_avg") or 0
    memory = utilization.get("memory_avg") or 0
    network = utilization.get("network_avg") or 0

    # 2️⃣ Compute rule-based risk score
    risk_score = compute_risk_score(cpu=cpu)

    # 3️⃣ Classify rule-based risk
    risk_level = classify_risk(risk_score)

    # 4️⃣ Build ML feature vector
    features = {
        "cpu_avg": cpu,
        "memory_avg": memory,
        "network_avg": network,
        "estimated_monthly_savings": getattr(plan, "estimated_monthly_savings", 0),
        "risk_score": risk_score,
        "execution_time_seconds": 5,
    }

    # 5️⃣ AI prediction layer
    ml_allows = predict_execution(features)

    # 6️⃣ Final decision
    auto_execute = risk_level == "SAFE" and ml_allows

    decision = Decision.objects.create(
        plan=plan,
        risk_score=risk_score,
        risk_level=risk_level,
        auto_execute_allowed=auto_execute,
        reason=f"risk={risk_score:.2f}, level={risk_level}, ml={ml_allows}",
    )

    return decision, utilization