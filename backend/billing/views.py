# billing/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .models import SavingsLedger, SavingsAttribution
from .serializers import SavingsAttributionSerializer, InvoiceLineItemSerializer
from .permissions import IsInternalService


class SavingsSummaryView(APIView):
    permission_classes = [IsInternalService]

    def get(self, request):
        account = request.query_params.get("account")
        period = request.query_params.get("period")  # YYYY-MM

        if not account or not period:
            return Response({"error": "Missing parameters"}, status=400)

        total = SavingsLedger.objects.filter(
            cloud_account_id=account,
            period_start__startswith=period,
        ).aggregate(total=Sum("amount"))["total"] or 0

        return Response({
            "account": account,
            "period": period,
            "total_savings": round(total, 2),
            "currency": "USD",
        })


class SavingsResourceBreakdownView(APIView):
    permission_classes = [IsInternalService]

    def get(self, request):
        execution_id = request.query_params.get("execution_id")

        attributions = SavingsAttribution.objects.filter(
            execution_id=execution_id
        )

        serializer = SavingsAttributionSerializer(attributions, many=True)
        return Response(serializer.data)


class SavingsInvoiceView(APIView):
    permission_classes = [IsInternalService]

    def get(self, request):
        account = request.query_params.get("account")
        month = request.query_params.get("month")

        qs = SavingsLedger.objects.filter(
            cloud_account_id=account,
            period_start__startswith=month,
        ).order_by("period_start")

        serializer = InvoiceLineItemSerializer(qs, many=True)
        return Response({
            "account": account,
            "month": month,
            "items": serializer.data,
        })
