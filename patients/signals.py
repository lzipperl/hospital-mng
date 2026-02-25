from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from .models import Patient


@receiver(post_save, sender=Patient)
def ensure_patient_role(sender, instance: Patient, created: bool, **kwargs):
    if not instance.user:
        return
    if instance.user.role != User.Roles.PATIENT:
        instance.user.role = User.Roles.PATIENT
        instance.user.save(update_fields=["role"])

