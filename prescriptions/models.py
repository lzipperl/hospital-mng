from django.db import models

from appointments.models import Appointment
from doctors.models import Doctor


class Prescription(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="prescription",
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="prescriptions",
    )
    medications = models.TextField(help_text="List medications and doses")
    instructions = models.TextField(blank=True)
    follow_up_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Prescription for {self.appointment}"
