from datetime import date
from decimal import Decimal
from django.contrib import admin
from django.db.models import F
from .models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "loanee",
        "amount",
        "amount_due",
        "interest",
        "is_paid",
        "is_due",
        "date_borrowed",
        "date_paid",
    )
    list_filter = (
        "loanee",
        "is_due",
        "is_paid",
        "date_borrowed",
        "date_paid",
    )
    ordering = (
        "is_paid",
        "date_borrowed",
        "loanee",
        "amount",
        "amount_due",
        "date_paid",
    )
    search_fields = ["loanee"]

    def get_queryset(self, request):
        """Automatically update `is_due` for each record in the queryset."""
        queryset = super().get_queryset(request)
        queryset.filter(is_paid=False, date_borrowed__lte=date.today()).update(
            is_due=True
        )
        queryset.filter(is_paid=False, amount_due=0).update(
            is_due=False, is_paid=True, date_paid=date.today()
        )
        queryset.filter(is_paid=True).update(is_due=False)

        return queryset
