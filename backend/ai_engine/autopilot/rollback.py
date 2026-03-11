# ai_engine/autopilot/rollback.py

from monitoring.health import health_failed
from actions.models import ActionExecution


def rollback_if_needed(organization):
    """
    Trigger rollback if post-action health checks fail.
    """
    if not health_failed(organization):
        return False

    failed_actions = ActionExecution.objects.filter(
        action_plan__resource__cloud_account__organization=organization,
        status="success",
    ).order_by("-executed_at")[:3]  # bounded rollback

    for execution in failed_actions:
        rollback_action(execution)

    return True



def rollback_action(execution: ActionExecution):
    plan = execution.action_plan
    resource = plan.resource

    if plan.action_type == "stop_instance":
        rollback_stop_instance(resource)

    elif plan.action_type == "resize_volume":
        rollback_resize_volume(resource)

    elif plan.action_type == "delete_snapshot":
        # snapshots are irreversible → mark only
        mark_unrecoverable(execution)

    execution.status = "rolled_back"
    execution.save()


def rollback_stop_instance(resource):
    """
    Restart EC2 instance.
    """
    from cloud.aws.ec2 import start_instance
    start_instance(resource.external_id)


def rollback_resize_volume(resource):
    """
    Resize back to previous size.
    """
    previous_size = resource.metadata.get("previous_size_gb")
    if not previous_size:
        return

    from cloud.aws.ebs import resize_volume
    resize_volume(resource.external_id, previous_size)


def mark_unrecoverable(execution):
    execution.error_message = "Rollback not possible for snapshot deletion"
