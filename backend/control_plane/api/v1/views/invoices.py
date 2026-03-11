# control_plane/api/v1/views/invoices.py

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from control_plane.permissions.member import IsOrganizationMember
from billing.models import Invoice


class InvoiceListView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        invoices = Invoice.objects.filter(
            organization=request.organization
        ).order_by("-period")

        return Response([
            {
                "id": inv.id,
                "number": f"INV-{inv.id}",
                "month": inv.period,
                "amount": inv.platform_fee,
                "status": inv.status,
            }
            for inv in invoices
        ])
