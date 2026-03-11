# ai_engine/right_sizing.py

from ai_engine.instance_families import smaller_instance
from ai_engine.utilization import utilization_profile
from ai_engine.resize_rules import resize_safe
from actions.models import ActionPlan


def generate_resize_plan(resource):
    instance_type = resource.metadata.get("InstanceType")
    target = smaller_instance(instance_type)

    if not target:
        return None

    utilization = utilization_profile(resource)
    safe, reason = resize_safe(resource, utilization)

    if not safe:
        return None

    return ActionPlan.objects.create(
        resource=resource,
        action_type="resize",
        estimated_savings=resource.cost_per_hour * 0.5 * 24 * 30,
        risk_level="low",
        is_safe=True,
        explanation=(
            f"Instance underutilized (avg CPU {utilization['cpu_avg']:.1f}%). "
            f"Safe resize from {instance_type} → {target}."
        ),
    )
