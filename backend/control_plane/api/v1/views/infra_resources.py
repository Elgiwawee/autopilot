# control_plane/api/v1/views/infra_regions.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cloud.models import CloudResource
from control_plane.permissions.member import IsOrganizationMember


class ResourceListView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        org = request.organization

        region = request.query_params.get("region")
        resource_type = request.query_params.get("type")

        queryset = CloudResource.objects.filter(
            cloud_account__organization=org
        ).select_related("cloud_account", "provider")

        if region:
            queryset = queryset.filter(region=region)

        if resource_type:
            queryset = queryset.filter(resource_type=resource_type)

        results = []

        for r in queryset:
            results.append({
                "id": str(r.id),
                "external_id": r.external_id,
                "type": r.resource_type,
                "region": r.region,
                "state": r.state,
                "provider": r.provider.display_name,
                "monthly_cost": float(r.cost_per_hour) * 24 * 30,
            })

        return Response({
            "count": len(results),
            "results": results,
        })