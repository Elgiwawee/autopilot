from django.http import HttpResponse
from billing.models import Invoice
from billing.permissions import IsInternalService
from billing.services.exports import export_invoice_csv
from billing.services.pdf import export_invoice_pdf


class InvoiceExportView(APIView):
    permission_classes = [IsInternalService]

    def get(self, request, invoice_id, fmt):
        invoice = Invoice.objects.get(id=invoice_id)

        if fmt == "csv":
            data = export_invoice_csv(invoice)
            return HttpResponse(
                data,
                content_type="text/csv",
            )

        if fmt == "pdf":
            pdf = export_invoice_pdf(invoice)
            return HttpResponse(
                pdf,
                content_type="application/pdf",
            )
