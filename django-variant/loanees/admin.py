from django.contrib import admin
from .models import Loanee


@admin.register(Loanee)
class LoaneeAdmin(admin.ModelAdmin):
    list_display = ("name", "total_due")

    # list_filter = ()
    ordering = ["name"]
    search_fields = ["name"]
