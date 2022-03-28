from django.db import models
from colorfield.fields import ColorField

from beverage.managers import BeverageManager
from stock_price.models import StockPrice


class Beverage(models.Model):
    name = models.CharField(max_length=50)
    color = ColorField()
    number_of_sales = models.IntegerField(default=0)
    retail_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Price, for which the beverage has been bought",
    )
    price_weight = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Price-Weight - calculated by dividing the sum of all prices by the beverages retail_price",
    )

    objects = BeverageManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "name",
        ]

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.create_default_stock_price_if_not_existent()

        return super().save(force_insert, force_update, using, update_fields)

    def create_default_stock_price_if_not_existent(self):
        if self.stock_prices.exists():
            return

        StockPrice.objects.create(price=self.retail_price + 1, beverage=self)

    @property
    def current_stock_price(self):
        return self.stock_prices.first().price
