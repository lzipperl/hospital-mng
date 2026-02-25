from rest_framework import permissions, viewsets

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.select_related("user").all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

