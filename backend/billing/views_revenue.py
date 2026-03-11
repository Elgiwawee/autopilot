# billing/views_revenue.py


from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from billing.models import RevenueShare
from billing.permissions import IsInternalService


class RevenueSummaryView(APIView):
    permission_classes = [IsInternalService]

    def get(self, request):
        qs = RevenueShare.objects.all()

        return Response({
            "total_due": qs.filter(paid=False).aggregate(
                total=Sum("amount_due")
            )["total"] or 0,
            "total_paid": qs.filter(paid=True).aggregate(
                total=Sum("amount_due")
            )["total"] or 0,
        })
