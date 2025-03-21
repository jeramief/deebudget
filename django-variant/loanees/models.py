from django.db import models


class Loanee(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_due(self):
        """Calculate the total outstanding loan amount."""
        return sum(
            loan.amount_due for loan in self.loans.filter(is_due=True, is_paid=False)
        )

    def __str__(self):
        return self.name
