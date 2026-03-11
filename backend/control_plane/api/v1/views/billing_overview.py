# control_plane/views/billing_overview.py

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from control_plane.permissions.member import IsOrganizationMember

from control_plane.services.billing_service import build_billing_overview


class BillingOverviewView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]


    def get(self, request):
        organization = request.organization
        data = build_billing_overview(organization)
        return Response(data)
