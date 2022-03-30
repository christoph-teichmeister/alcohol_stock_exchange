from django.db import models

from core import settings


class Stock(models.Model):
    amount = models.IntegerField(default=0)
    beverage = models.ForeignKey(
        settings.BEVERAGE_MODEL,
        related_name="stock",
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f"Stock of {self.beverage.name} ({self.amount})"

    class Meta:
        ordering = ["beverage"]
