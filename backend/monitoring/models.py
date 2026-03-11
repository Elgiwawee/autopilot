# monitoring/models.py

from django.db import models
from django.utils import timezone
import accounts
import cloud

class ResourceMetric(models.Model):
    resource = models.ForeignKey(
        "cloud.CloudResource", on_delete=models.CASCADE, related_name="metrics"
    )
    metric_name = models.CharField(max_length=64)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class MaintenanceWindow(models.Model):
    organization = models.ForeignKey(
        "accounts.Organization",
        on_delete=models.CASCADE,
    )

    start_time = models.TimeField()
    end_time = models.TimeField()
    timezone = models.CharField(max_length=64, default="UTC")

    allow_autopilot = models.BooleanField(default=True)


class ServiceSLO(models.Model):
    resource = models.ForeignKey(
        "cloud.CloudResource", on_delete=models.CASCADE
    )

    metric_name = models.CharField(max_length=64)  # latency, error_rate
    max_value = models.FloatField()


class NodeMetric(models.Model):
    cluster_id = models.CharField(max_length=128)
    node_name = models.CharField(max_length=128)

    cpu_used = models.FloatField()
    cpu_total = models.FloatField()

    mem_used = models.IntegerField()
    mem_total = models.IntegerField()

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["cluster_id", "node_name", "timestamp"])
        ]


class SLA(models.Model):
    service = models.CharField(max_length=128)
    max_latency_ms = models.IntegerField()
    max_error_rate = models.FloatField()


def sla_safe(metrics, sla):
    if metrics.p95_latency > sla.max_latency_ms:
        return False
    if metrics.error_rate > sla.max_error_rate:
        return False
    return True
