# control_plane/api/v1/views/infra_regions.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cloud.models import CloudResource
from control_plane.permissions.member import IsOrganizationMember


class RegionsView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        org = request.organization

        regions = (
            CloudResource.objects
            .filter(cloud_account__organization=org)
            .values_list("region", flat=True)
            .distinct()
        )

        return Response({
            "results": list(regions)
        })