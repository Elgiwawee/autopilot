# cloud/services/pricing.py

from cloud.models import InstancePricing


def get_hourly_price(
    provider,
    instance_type,
    region,
    operating_system="linux",
    pricing_model="on_demand"
):
    try:
        pricing = InstancePricing.objects.get(
            provider=provider,
            instance_type=instance_type,
            region=region,
            operating_system=operating_system,
            pricing_model=pricing_model,
        )
        return float(pricing.price_per_hour)
    except InstancePricing.DoesNotExist:
        return 0