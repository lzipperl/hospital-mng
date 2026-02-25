from django.contrib import admin

from .models import Prescription


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "appointment", "doctor", "created_at")
