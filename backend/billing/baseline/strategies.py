# billing/baseline/strategies.py

from datetime import timedelta
from django.db.models import Avg
from billing.models import CostSnapshot

BASELINE_WINDOW_DAYS = 21


def rolling_average(resource_id, service, cloud_account, target_date):
    start_date = target_date - timedelta(days=BASELINE_WINDOW_DAYS)

    qs = CostSnapshot.objects.filter(
        cloud_account=cloud_account,
        service=service,
        resource_id=resource_id,
        date__gte=start_date,
        date__lt=target_date,
    )

    if not qs.exists():
        return None

    return qs.aggregate(avg=Avg("cost"))["avg"]


def weekday_average(resource_id, service, cloud_account, target_date):
    weekday = target_date.weekday()

    qs = CostSnapshot.objects.filter(
        cloud_account=cloud_account,
        service=service,
        resource_id=resource_id,
        date__week_day=weekday + 1,
        date__lt=target_date,
    ).order_by("-date")[:4]

    if not qs:
        return None

    return sum(s.cost for s in qs) / len(qs)
