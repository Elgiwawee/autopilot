# control_plane/api/v1/views/autopilot_settings.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from control_plane.permissions.member import IsOrganizationMember
from accounts.models import AutopilotSettings


class AutopilotSettingsView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        settings = AutopilotSettings.objects.filter(
            cloud_account__organization=request.organization
        )

        return Response([
            {
                "cloud_account": s.cloud_account.id,
                "mode": s.mode,
                "max_risk_allowed": s.max_risk_allowed,
            }
            for s in settings
        ])

    def post(self, request):
        # Later: validation, approvals, audit log
        cloud_account_id = request.data["cloud_account"]
        mode = request.data["mode"]
        max_risk = request.data["max_risk_allowed"]

        s = AutopilotSettings.objects.get(
            cloud_account_id=cloud_account_id,
            cloud_account__organization=request.organization
        )

        s.mode = mode
        s.max_risk_allowed = max_risk
        s.save()

        return Response({"status": "updated"})
