from django.db import models
from django.utils import timezone

from core import settings
from stock_price.managers import StockPriceManager


class StockPrice(models.Model):
    beverage = models.ForeignKey(
        settings.BEVERAGE_MODEL,
        related_name="stock_prices",
        on_delete=models.DO_NOTHING,
    )
    price = models.DecimalField(max_digits=4, decimal_places=2)
    timestamp = models.DateTimeField(
        default=timezone.now, help_text="Time at which this price has been issued"
    )

    objects = StockPriceManager()

    def __str__(self):
        return f"{self.price}€ : {self.beverage.name}"

    class Meta:
        ordering = ["-timestamp"]
