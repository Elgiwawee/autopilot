from accounts.models import Organization


class OrganizationContextMiddleware:
    """
    Attach organization to request based on auth context.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # TEMP: replace with real membership lookup
        if request.user and request.user.is_authenticated:
            request.organization = Organization.objects.first()
        else:
            request.organization = None

        return self.get_response(request)
