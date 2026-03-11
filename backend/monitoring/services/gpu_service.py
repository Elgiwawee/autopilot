# monitoring/services/gpu_service.py

from django.db.models import QuerySet
from cloud.models import CloudAccount, CloudResource


class GPUService:
    """
    Production-grade GPU inventory service
    """

    @staticmethod
    def _base_queryset(organization) -> QuerySet:
        """
        Returns base queryset of GPU resources for an organization.
        """

        active_accounts = CloudAccount.objects.filter(
            organization=organization,
            is_active=True,
        )

        return CloudResource.objects.filter(
            cloud_account__in=active_accounts,
            resource_type="gpu",
        ).select_related("provider", "cloud_account")

    # ----------------------------------------------------
    # Public Methods
    # ----------------------------------------------------

    @classmethod
    def list(
        cls,
        organization,
        cloud: str | None = None,
        region: str | None = None,
    ):
        qs = cls._base_queryset(organization)

        if cloud:
            qs = qs.filter(cloud_account__provider__slug=cloud)

        if region:
            qs = qs.filter(region=region)

        return [
            cls._serialize(resource)
            for resource in qs
        ]

    @classmethod
    def count(
        cls,
        organization,
        cloud: str | None = None,
        region: str | None = None,
    ) -> int:
        qs = cls._base_queryset(organization)

        if cloud:
            qs = qs.filter(cloud_account__provider__slug=cloud)

        if region:
            qs = qs.filter(region=region)

        return qs.count()

    # ----------------------------------------------------
    # Internal serializer
    # ----------------------------------------------------

    @staticmethod
    def _serialize(resource):
        return {
            "id": str(resource.id),
            "provider": resource.provider.name,
            "cloud_account": str(resource.cloud_account.id),
            "external_id": resource.external_id,
            "region": resource.region,
            "state": resource.state,
            "cost_per_hour": float(resource.cost_per_hour),
            "model": resource.metadata.get("model"),
            "memory_gb": resource.metadata.get("memory_gb"),
            "attached_to": resource.metadata.get("attached_to"),
            "last_seen": resource.last_seen,
        }