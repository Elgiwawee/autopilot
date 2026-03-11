# control_plane/services/registration_service.py

from django.contrib.auth import get_user_model
from django.db import transaction

from accounts.models import Organization, OrganizationMember, AutopilotPolicy

User = get_user_model()


@transaction.atomic
def register_customer(email, password, organization_name):
    # 1. Create user
    user = User.objects.create_user(
        email=email,
        password=password
    )

    # 2. Create organization
    org = Organization.objects.create(
        name=organization_name
    )

    # 3. Attach user to org
    OrganizationMember.objects.create(
        organization=org,
        user=user,
        role="OWNER"
    )

    # 4. Create default autopilot policy
    AutopilotPolicy.objects.create(
        organization=org
    )

    return user, org
