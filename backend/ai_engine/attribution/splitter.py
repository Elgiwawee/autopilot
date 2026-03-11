# ai_engine/attribution/splitter.py
from .weights import compute_weights
from billing.models import CostSnapshot

def split_service_cost(service_snapshot, resource_usages):
    compute_weights(resource_usages)

    for u in resource_usages:
        CostSnapshot.objects.update_or_create(
            cloud_account=service_snapshot.cloud_account,
            provider=service_snapshot.provider,
            service=service_snapshot.service,
            region=service_snapshot.region,
            resource_id=u.resource_id,
            date=service_snapshot.date,
            defaults={
                "cost": service_snapshot.cost * u.weight,
                "currency": "USD",
                "derived": True,
            }
        )
