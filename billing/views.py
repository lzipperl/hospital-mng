from django.db.models import Sum
from rest_framework import permissions, response, viewsets
from rest_framework.decorators import action

from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.select_related("appointment").all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def revenue_summary(self, request):
        total_revenue = (
            self.get_queryset()
            .filter(status=Invoice.Status.PAID)
            .aggregate(total=Sum("total"))["total"]
            or 0
        )
        return response.Response({"total_revenue": total_revenue})

