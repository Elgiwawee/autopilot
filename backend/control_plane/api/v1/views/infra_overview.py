# control_plane/api/v1/views/infra_overview.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cloud.models import CloudAccount, CloudResource
from control_plane.permissions.member import IsOrganizationMember


class InfraOverviewView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        org = request.organization

        accounts = CloudAccount.objects.filter(
            organization=org,
            is_active=True
        )

        resources = CloudResource.objects.filter(
            cloud_account__organization=org
        )

        total_accounts = accounts.count()

        total_regions = (
            resources.values("region")
            .distinct()
            .count()
        )

        total_resources = resources.count()

        total_monthly_cost = sum(
            float(r.cost_per_hour) * 24 * 30
            for r in resources
        )

        return Response({
            "accounts": total_accounts,
            "regions": total_regions,
            "resources": total_resources,
            "monthly_cost": round(total_monthly_cost, 2),
        })