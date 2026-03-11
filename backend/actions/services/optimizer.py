# actions/services/optimizer.py

from actions.models import OptimizationPlan


def list_optimizations(organization, cloud=None):
    qs = OptimizationPlan.objects.filter(
        cloud_account__organization=organization,
        status="PLANNED",
    ).select_related("cloud_account")

    # Optional cloud filter
    if cloud:
        qs = qs.filter(cloud_account__provider=cloud)

    # Optional region filter
    #if region:
    #    qs = qs.filter(region=region)

    return [
        {
            "id": str(opt.id),
            "cloud": opt.cloud_account.provider,
            "resource_type": opt.resource_type,
            "resource_id": opt.resource_id,
            "action": opt.action_type,
            "estimated_monthly_savings": float(opt.estimated_monthly_savings),
            "confidence": opt.confidence,
            "status": opt.status,
        }
        for opt in qs
    ]