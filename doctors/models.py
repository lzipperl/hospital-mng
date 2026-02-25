from django.conf import settings
from django.db import models


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
    )
    specialization = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user.get_full_name() or self.user.email} - {self.specialization}"
