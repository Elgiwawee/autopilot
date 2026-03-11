# control_plane/api/v1/views/global_safety.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import GlobalSafety


class GlobalSafetyStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gs = GlobalSafety.objects.first()

        return Response({
            "autopilot_enabled": bool(
                gs and gs.autopilot_enabled
            )
        })
