# control_plane/api/v1/views/infra_cloud_accounts.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cloud.models import CloudAccount, CloudResource
from control_plane.permissions.member import IsOrganizationMember


class InfraCloudAccountView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        org = request.organization

        accounts = CloudAccount.objects.filter(
            organization=org,
            is_active=True
        ).select_related("provider")

        results = []

        for acc in accounts:
            resources = CloudResource.objects.filter(
                cloud_account=acc
            )

            monthly_cost = sum(
                float(r.cost_per_hour) * 24 * 30
                for r in resources
            )

            results.append({
                "id": str(acc.id),
                "provider": acc.provider.display_name,
                "account_identifier": acc.account_identifier,
                "mode": acc.mode,
                "resource_count": resources.count(),
                "monthly_cost": round(monthly_cost, 2),
            })

        return Response({
            "results": results
        })