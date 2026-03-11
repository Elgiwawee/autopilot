# actions/services/action_service.py

from actions.models import ActionExecution


class ActionService:

    @staticmethod
    def _base_queryset(organization):
        return (
            ActionExecution.objects.filter(
                action_plan__resource__cloud_account__organization=organization
            )
            .select_related(
                "action_plan",
                "action_plan__resource",
                "action_plan__resource__cloud_account",
                "action_plan__resource__cloud_account__provider",
            )
        )

    @classmethod
    def recent(cls, organization, cloud=None, region=None, limit=10):
        qs = cls._base_queryset(organization)

        if cloud:
            qs = qs.filter(
                action_plan__resource__cloud_account__provider__slug=cloud
            )

        if region:
            qs = qs.filter(
                action_plan__resource__cloud_account__region=region
            )

        qs = qs.order_by("-executed_at")[:limit]

        return [
            {
                "id": str(a.id),
                "status": a.status,
                "executed_at": a.executed_at,
                "cloud": (
                    a.action_plan.resource.cloud_account.provider.slug
                    if a.action_plan and a.action_plan.resource
                    else None
                ),
            }
            for a in qs
        ]