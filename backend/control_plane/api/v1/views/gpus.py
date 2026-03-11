# control_plane/api/v1/views/gpus.py

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from control_plane.permissions.member import IsOrganizationMember
from control_plane.services.gpu_service import GPUInventoryService


class GPUView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        organization = request.organization

        cloud = request.query_params.get("cloud")
        region = request.query_params.get("region")

        data = GPUInventoryService.build(
            organization=organization,
            cloud=cloud,
            region=region,
        )

        return Response(data)