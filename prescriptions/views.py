from rest_framework import permissions, viewsets

from .models import Prescription
from .serializers import PrescriptionSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.select_related("appointment", "doctor").all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

