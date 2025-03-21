from datetime import date
from django.core.validators import MinValueValidator
from django.db import models
from loans.models import Loan


class Payment(models.Model):
    loan = models.ForeignKey(
        "loans.Loan", on_delete=models.CASCADE, related_name="payments"
    )
    amount_paid = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    payment_method = models.CharField(max_length=50, blank=False)
    date_paid = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        """Reduce loan's `amount_due` when a payment is made"""
        super().save(*args, **kwargs)

        self.loan.amount_due -= self.amount_paid
        self.loan.save()
