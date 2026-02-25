from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from .models import Doctor


@receiver(post_save, sender=Doctor)
def ensure_doctor_role(sender, instance: Doctor, created: bool, **kwargs):
    if not instance.user:
        return
    if instance.user.role != User.Roles.DOCTOR:
        instance.user.role = User.Roles.DOCTOR
        instance.user.save(update_fields=["role"])

