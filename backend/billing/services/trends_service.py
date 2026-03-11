# billing/services/trends_service.py

from django.db.models import Sum
from billing.models import CostSnapshot


class TrendService:

    @classmethod
    def cost_trend(
        cls,
        organization,
        cloud: str | None = None,
        region: str | None = None,
        days: int = 7,
    ):
        """
        Returns aggregated daily cost trend for an organization.
        """

        qs = CostSnapshot.objects.filter(
            cloud_account__organization=organization
        )

        # Filter by cloud provider (AWS | GCP | AZURE)
        if cloud:
            qs = qs.filter(
                provider__iexact=cloud
            )

        # Filter by region
        if region:
            qs = qs.filter(
                region__iexact=region
            )

        # Aggregate cost per date
        qs = (
            qs.values("date")
            .annotate(total_cost=Sum("cost"))
            .order_by("-date")[:days]
        )

        # Reverse so oldest first
        trend = list(reversed(qs))

        return [
            {
                "date": row["date"],
                "cost": float(row["total_cost"] or 0),
            }
            for row in trend
        ]