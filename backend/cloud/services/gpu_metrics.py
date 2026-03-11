# cloud/services/gpu_metrics.py

from datetime import timedelta, date
from cloud.providers.factory import get_provider


def get_gpu_utilization(cloud_account, resource_ids):
    provider = get_provider(cloud_account)

    end = date.today()
    start = end - timedelta(days=1)

    # GPU utilization will be CPU proxy for now
    metrics = provider.fetch_metrics(
        resource_ids=resource_ids,
        metric_name="CPUUtilization",
        start_date=start,
        end_date=end,
    )

    utilization = {}

    for m in metrics:
        rid = m["resource_id"]
        values = [p["value"] for p in m.get("datapoints", [])]

        utilization[rid] = (
            sum(values) / len(values) if values else 0
        )

    return utilization
