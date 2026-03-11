# ai_engine/spot/models.py

from django.db import models

class SpotInterruption(models.Model):
    instance_type = models.CharField(max_length=64)
    availability_zone = models.CharField(max_length=32)
    interrupted = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
