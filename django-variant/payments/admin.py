from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "amount_paid",
        "loan__loanee__name",
        "loan_amount_due",
        "loan__amount",
        "date_paid",
        "loan__date_borrowed",
    ]

    # @admin.display(ordering="loan__loanee__name", description="Loanee")
    # def loanee_name(self, obj):
    #     return obj.loan.loanee.name if obj.loan and obj.loan.loanee else "N/A"

    @admin.display(ordering="loan__amount_due", description="Amount Left Due")
    def loan_amount_due(self, obj):
        return obj.loan.amount_due if obj.loan else "N/A"

    # @admin.display(ordering="loan__amount", description="Total Amount")
    # def loan_amount(self, obj):
    #     return obj.loan.amount if obj.loan else "N/A"

    # @admin.display(ordering="loan__date_borrowed", description="Date Borrowed")
    # def loan_date_borrowed(self, obj):
    #     return obj.loan.date_borrowed if obj.loan else "N/A"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("loan")
