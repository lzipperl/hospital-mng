from rest_framework import permissions, viewsets

from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related("doctor", "patient").all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

