# audit/services/receipt.py
def generate_execution_receipt(execution):
    decision = execution.decision

    return {
        "what": f"Stopped EC2 {decision.plan.resource_id}",
        "why": decision.reason,
        "risk_score": decision.risk_score,
        "who": "AUTOPILOT",
        "when": execution.finished_at.isoformat(),
        "rollback_available": execution.state != "COMPLETED",
        "savings_estimate": decision.plan.estimated_savings,
    }
