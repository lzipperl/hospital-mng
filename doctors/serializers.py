from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    user_email = serializers.EmailField(source="user.email", read_only=True)
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)

    class Meta:
        model = Doctor
        fields = [
            "id",
            "user_id",
            "user_email",
            "user_name",
            "specialization",
            "experience_years",
            "bio",
            "is_active",
        ]

