from django.db import models
from django.db.models import F

from appointments.models import Appointment


class Invoice(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PAID = "PAID", "Paid"
        CANCELLED = "CANCELLED", "Cancelled"

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="invoice",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    issued_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = (self.amount - self.discount) + self.tax
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Invoice #{self.pk} for {self.appointment}"
