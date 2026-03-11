# billing/views_invoices.py


from rest_framework.views import APIView
from rest_framework.response import Response

from billing.models import Invoice
from billing.permissions import IsInternalService
from billing.serializers import InvoiceSerializer


class InvoiceListView(APIView):
    permission_classes = [IsInternalService]

    def get(self, request):
        org_id = request.query_params.get("organization")

        qs = Invoice.objects.filter(
            organization_id=org_id
        ).order_by("-period")

        serializer = InvoiceSerializer(qs, many=True)
        return Response(serializer.data)
