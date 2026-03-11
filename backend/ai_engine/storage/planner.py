# ai_engine/storage/planner.py

from actions.models import ActionPlan

def generate_gp3_plan(volume):
    savings = volume.size_gb * 0.02 * 24 * 30  # conservative

    return ActionPlan.objects.create(
        resource_type="ebs",
        resource_id=volume.id,
        action_type="convert_gp2_to_gp3",
        estimated_savings=savings,
        risk_level="low",
        is_safe=True,
        explanation=(
            f"EBS volume {volume.volume_id} is GP2. "
            "GP3 offers lower cost with same or better performance."
        ),
    )
