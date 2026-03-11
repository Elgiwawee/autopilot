# ai_engine/models.py

from django.db import models
from cloud.models import CloudAccount

# Create your models here.
class Recommendation(models.Model):
    resource = models.ForeignKey(
        "cloud.CloudResource", on_delete=models.CASCADE
    )
    recommendation_type = models.CharField(max_length=64)
    expected_monthly_savings = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    confidence = models.FloatField()
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ResourceUsage(models.Model):
    cloud_account = models.ForeignKey(
        CloudAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="resource_usages"
    )
    resource_id = models.CharField(max_length=255)
    service = models.CharField(max_length=50)  # EC2 / EKS
    date = models.DateField()

    cpu_hours = models.FloatField(default=0)
    memory_gb_hours = models.FloatField(default=0)

    weight = models.FloatField()  # normalized later


class AutopilotRun(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=["organization", "started_at"]),
        ]

    organization = models.ForeignKey(
        'accounts.Organization',
        on_delete=models.CASCADE
    )

    started_at = models.DateTimeField(auto_now_add=True)

    finished_at = models.DateTimeField(
        null=True,
        blank=True
    )

    plans_generated = models.IntegerField(default=0)

    plans_executed = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        default="running"
    )

class ActionOutcome(models.Model):
    """
    Dataset used to train the learning models.
    Each row represents the outcome of an executed action.
    """

    organization = models.ForeignKey(
        "accounts.Organization",
        on_delete=models.CASCADE,
        related_name="action_outcomes"
    )

    cloud_account = models.ForeignKey(
        "cloud.CloudAccount",
        on_delete=models.CASCADE,
        related_name="action_outcomes"
    )

    resource_type = models.CharField(max_length=50)
    resource_id = models.CharField(max_length=255)

    action_type = models.CharField(max_length=50)

    before_state = models.JSONField()
    after_state = models.JSONField(null=True, blank=True)

    estimated_savings = models.FloatField(default=0)

    success = models.BooleanField(default=False)

    execution_time_seconds = models.FloatField(null=True, blank=True)

    failure_reason = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["resource_type"]),
            models.Index(fields=["action_type"]),
        ]