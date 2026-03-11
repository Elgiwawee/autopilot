# control_plane/api/v1/views/auth.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from control_plane.services.registration_service import register_customer
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError

class RegisterView(APIView):
    authentication_classes = []

    def post(self, request):
        try:
            user, org = register_customer(
                email=request.data.get("email"),
                password=request.data.get("password"),
                organization_name=request.data.get("organization_name"),
            )
        except IntegrityError:
            return Response(
                {"detail": "Email already registered"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"message": "Registration successful"},
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            raise AuthenticationFailed("Email and password required")

        user = authenticate(request, username=email, password=password)

        if not user:
            raise AuthenticationFailed("Invalid credentials")

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
            }
        })