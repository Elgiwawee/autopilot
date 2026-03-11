# actions/services/executions.py

from actions.models import ExecutionPlan


def get_recent_actions(organization, limit=10):
    """
    Read-only execution history for dashboards.
    """

    return list(
        ExecutionPlan.objects
        .filter(cloud_account__organization=organization)
        .order_by("-created_at")[:limit]
    )
