# control_plane/views/invoice_export.py

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from control_plane.permissions.member import IsOrganizationMember
from billing.services.exports import export_invoice_csv
from billing.services.pdf import export_invoice_pdf


class InvoiceExportView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request, invoice_id, fmt):
        if fmt == "csv":
            file_data = export_invoice_csv(
                request.organization,
                invoice_id
            )
            return HttpResponse(file_data, content_type="text/csv")

        if fmt == "pdf":
            buffer = export_invoice_pdf(
                request.organization,
                invoice_id
            )
            return HttpResponse(buffer, content_type="application/pdf")

        return Response({"error": "Invalid format"}, status=400)