from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            "id",
            "appointment",
            "amount",
            "discount",
            "tax",
            "total",
            "status",
            "issued_at",
            "paid_at",
        ]
        read_only_fields = ["id", "total", "issued_at", "paid_at"]

from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            "id",
            "appointment",
            "amount",
            "status",
            "issued_at",
            "updated_at",
        ]
        read_only_fields = ["id", "issued_at", "updated_at"]

