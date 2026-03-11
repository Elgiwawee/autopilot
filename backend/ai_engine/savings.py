# ai_engine/savings.py

from ai_engine.baseline import baseline_cost

def calculate_savings(execution, actual_cost, date):
    baseline = baseline_cost(
        resource_id=execution.decision.plan.resource.external_id,
        service=execution.decision.plan.resource.service,
        cloud_account=execution.decision.plan.resource.cloud_account,
        target_date=date,
    )

    if baseline is None:
        return None

    savings = max(baseline - actual_cost, 0)

    return baseline, savings
