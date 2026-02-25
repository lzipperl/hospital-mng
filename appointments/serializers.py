from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_id = serializers.IntegerField(source="doctor.id", read_only=True)
    patient_id = serializers.IntegerField(source="patient.id", read_only=True)

    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "doctor_id",
            "patient",
            "patient_id",
            "scheduled_at",
            "status",
            "reason",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

from rest_framework import serializers

from accounts.serializers import DoctorSerializer, PatientSerializer
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(
        source="doctor", queryset=Appointment._meta.get_field("doctor").remote_field.model.objects.all(), write_only=True
    )
    patient_id = serializers.PrimaryKeyRelatedField(
        source="patient", queryset=Appointment._meta.get_field("patient").remote_field.model.objects.all(), write_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "patient",
            "doctor_id",
            "patient_id",
            "scheduled_at",
            "status",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "status"]

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["created_by"] = request.user
        return super().create(validated_data)

