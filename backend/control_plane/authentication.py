from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import OrganizationMember


class OrganizationJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        result = super().authenticate(request)

        if not result:
            return None

        user, token = result

        membership = (
            OrganizationMember.objects
            .select_related("organization")
            .filter(user=user)
            .first()
        )

        request.organization = (
            membership.organization if membership else None
        )

        return (user, token)