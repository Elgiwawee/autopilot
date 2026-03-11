# control_plane/aip/v1/views/cloud_accounts.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from cloud.models import CloudAccount, CloudProvider
from control_plane.permissions.member import IsOrganizationMember
from control_plane.tasks import discover_cloud_account

class CloudAccountListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def get(self, request):
        org = request.organization

        accounts = (
            CloudAccount.objects
            .filter(organization=org, is_active=True)
            .select_related("provider")
        )

        results = [
            {
                "id": str(acc.id),
                "provider": acc.provider.display_name,
                "provider_code": acc.provider.code,
                "account_identifier": acc.account_identifier,
                "mode": acc.mode,
                "status": "active" if acc.is_active else "disabled",
                "created_at": acc.created_at,
            }
            for acc in accounts
        ]

        return Response({"results": results})

    def post(self, request):
        org = request.organization

        provider_code = request.data.get("provider_code")
        account_identifier = request.data.get("account_identifier")
        role_arn = request.data.get("role_arn")
        mode = request.data.get("mode", "observe")

        if not provider_code or not account_identifier:
            return Response(
                {"detail": "Missing required fields"},
                status=status.HTTP_400_BAD_REQUEST
            )

        provider = get_object_or_404(
            CloudProvider,
            code=provider_code,
            is_active=True
        )

        cloud_account = CloudAccount.objects.create(
            organization=org,
            provider=provider,
            account_identifier=account_identifier,
            role_arn=role_arn,
            mode=mode,
            is_active=True,
        )
        # Trigger async infrastructure discovery
        discover_cloud_account.delay(cloud_account.id)

        return Response(
            {
                "id": str(cloud_account.id),
                "provider": cloud_account.provider.display_name,
                "provider_code": cloud_account.provider.code,
                "account_identifier": cloud_account.account_identifier,
                "mode": cloud_account.mode,
                "status": "active",
                "created_at": cloud_account.created_at,
            },
            status=status.HTTP_201_CREATED
        )
    
class CloudAccountDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizationMember]

    def delete(self, request, account_id):
        org = request.organization

        cloud_account = get_object_or_404(
            CloudAccount,
            id=account_id,
            organization=org,
        )

            # Soft delete
        cloud_account.is_active = False
        cloud_account.save(update_fields=["is_active"])

        return Response(
            {"detail": "Cloud account disabled"},
            status=status.HTTP_200_OK
        )