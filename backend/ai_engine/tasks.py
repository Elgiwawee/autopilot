# ai_engine/tasks.py

from celery import shared_task
from ai_engine.attribution.splitter import split_service_cost
from cloud.models import ServiceCostSnapshot

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=60)
def run_attribution(self, snapshot_id):
    snapshot = ServiceCostSnapshot.objects.get(id=snapshot_id)

    usages = ResourceUsage.objects.filter(
        cloud_account=snapshot.cloud_account,
        service=snapshot.service,
        date=snapshot.date,
    )

    split_service_cost(snapshot, usages)
