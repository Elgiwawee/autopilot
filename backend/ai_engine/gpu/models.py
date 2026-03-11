# ai_engine/gpu/models.py

from django.db import models

class GPUMetric(models.Model):
    workload_id = models.CharField(max_length=128)

    utilization = models.FloatField()
    mem_used = models.IntegerField()
    mem_total = models.IntegerField()

    timestamp = models.DateTimeField(auto_now_add=True)
