from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    user_email = serializers.EmailField(source="user.email", read_only=True)
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id",
            "user_id",
            "user_email",
            "user_name",
            "date_of_birth",
            "gender",
            "address",
            "phone",
            "emergency_contact",
        ]

