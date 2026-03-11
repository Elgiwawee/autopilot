# control_plane/serializers/overview.py

from rest_framework import serializers

class OverviewSerializer(serializers.Serializer):
    ai_status = serializers.DictField()
    kpis = serializers.DictField()
    cost_trend = serializers.ListField()
    recent_actions = serializers.ListField()
