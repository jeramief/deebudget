from datetime import date
from django.core.validators import MinValueValidator
from django.db import models


class Loan(models.Model):
    loanee = models.ForeignKey(
        "loanees.Loanee", on_delete=models.CASCADE, related_name="loans"
    )
    description = models.CharField(max_length=255)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00, validators=[MinValueValidator(0)]
    )
    amount_due = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00, validators=[MinValueValidator(0)]
    )
    interest = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.00, validators=[MinValueValidator(0)]
    )
    is_due = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    date_borrowed = models.DateField(default=date.today)
    date_paid = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.loanee} loaned {self.amount} {self.date_borrowed} - {self.amount_due} remaining"
