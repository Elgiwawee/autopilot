# billing/permissions.py
from django.conf import settings
from rest_framework.permissions import BasePermission

class IsInternalService(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get("X-Internal-Token") == settings.INTERNAL_API_TOKEN
