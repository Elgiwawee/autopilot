from actions.models import ActionPlan
from ai_engine.policies import autopilot_policy_check


def create_stop_instance_plan(resource):
    allowed, reason = autopilot_policy_check(resource, "stop")

    if not allowed:
        return None

    monthly_savings = resource.cost_per_hour * 24 * 30

    return ActionPlan.objects.create(
        resource=resource,
        action_type="stop",
        estimated_savings=monthly_savings,
        risk_level="low",
        is_safe=True,
        explanation=(
            "Instance idle for 14 days with CPU < 5%. "
            "Stopping will not delete data."
        ),
    )
