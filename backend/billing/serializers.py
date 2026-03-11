# billing/serializers.py

from rest_framework import serializers
from .models import SavingsLedger, SavingsAttribution, Invoice, InvoiceLineItem


class SavingsSummarySerializer(serializers.Serializer):
    account = serializers.UUIDField()
    period = serializers.CharField()
    total_savings = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField()


class SavingsAttributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsAttribution
        fields = [
            "resource_id",
            "baseline_cost",
            "actual_cost",
            "gross_savings",
            "net_savings",
            "confidence",
            "explanation",
        ]


class InvoiceLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsLedger
        fields = [
            "period_start",
            "period_end",
            "amount",
            "currency",
            "checksum",
        ]


class InvoiceLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLineItem
        fields = [
            "gross_savings",
            "platform_fee",
        ]


class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceLineItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = [
            "id",
            "period",
            "total_savings",
            "platform_fee",
            "currency",
            "status",
            "issued_at",
            "paid_at",
            "items",
        ]
