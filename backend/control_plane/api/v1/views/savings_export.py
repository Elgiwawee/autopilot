# control_plane/api/v1/views/savings_export.py

import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from control_plane.permissions.member import IsOrganizationMember
from actions.services.optimizer import list_optimizations


class SavingsExportCSVView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        organization = request.organization
        cloud = request.query_params.get("cloud")

        recs = list_optimizations(organization, cloud=cloud)

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="savings.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "Cloud",
            "Resource Type",
            "Resource ID",
            "Action",
            "Estimated Monthly Savings",
            "Confidence",
            "Status",
        ])

        for r in recs:
            writer.writerow([
                r["cloud"],
                r["resource_type"],
                r["resource_id"],
                r["action"],
                r["estimated_monthly_savings"],
                r["confidence"],
                r["status"],
            ])

        return response