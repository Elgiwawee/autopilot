from django.db import models


class ResourceFeature(models.Model):
    """
    Production-grade feature store entry.
    Each row represents a feature snapshot used for ML.
    """

    resource_id = models.CharField(max_length=255, db_index=True)
    resource_type = models.CharField(max_length=100, db_index=True)

    # utilization metrics
    cpu_avg = models.FloatField(null=True)
    memory_avg = models.FloatField(null=True)
    network_avg = models.FloatField(null=True)

    # economic signals
    estimated_monthly_savings = models.FloatField(default=0)

    # risk signals
    risk_score = models.FloatField(null=True)

    # execution signals
    execution_time_seconds = models.IntegerField(default=0)

    # training label
    action_success = models.BooleanField(null=True)

    # feature versioning
    feature_version = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["resource_id"]),
            models.Index(fields=["resource_type"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.resource_type}:{self.resource_id}"