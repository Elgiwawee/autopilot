# cloud/services/infra.py

from cloud.providers.factory import get_provider
from cloud.models import CloudResource


def sync_cloud_account_resources(cloud_account):
    """
    Pull resources from provider and store in DB.
    """
    provider = get_provider(cloud_account)

    resources = provider.get_region_resources()

    for resource in resources:
        CloudResource.objects.update_or_create(
            cloud_account=cloud_account,
            external_id=resource["id"],
            defaults={
                "provider": cloud_account.provider,
                "resource_type": resource["type"],
                "region": resource["region"],
                "state": resource["state"],
                "cost_per_hour": resource.get("cost_per_hour", 0),
                "metadata": resource,
            }
        )