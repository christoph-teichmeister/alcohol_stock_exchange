from django.db import models
from colorfield.fields import ColorField

from beverage.managers import BeverageManager
from core.helpers import get_stock_price_model, get_stock_model

StockPrice = get_stock_price_model()
Stock = get_stock_model()


class Beverage(models.Model):
    name = models.CharField(max_length=50)
    color = ColorField()
    number_of_sales = models.IntegerField(default=0)
    retail_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Price, for which the beverage has been bought",
    )
    number_of_sales_before_price_falls_by_one_euro = models.DecimalField(
        default=1,
        max_digits=4,
        decimal_places=2,
        help_text="Defines how many sales are made before the price has fallen by a full euro. \n"
        "Note: Price will fall before this number is reached too! \n"
        "Think of it like the following mathematical function: \n"
        "f(x) = 1/{number_of_sales_before_price_falls_by_one_euro}x + {retail_price} \n"
        "where 'x' is the beverages number_of_sales / total_sales. \n"
        "The price will hence never fall below the retail price but will slide along the linear graph.",
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
        self.create_default_stock_if_not_existent()

        return super().save(force_insert, force_update, using, update_fields)

    def create_default_stock_price_if_not_existent(self):
        if self.stock_prices.exists():
            return

        StockPrice.objects.create(price=self.retail_price + 1, beverage=self)

    def create_default_stock_if_not_existent(self):
        if self.stock.exists():
            return

        Stock.objects.create(amount=10, beverage=self)

    @property
    def current_stock_price(self):
        return self.stock_prices.first().price

    @property
    def current_stock(self):
        return self.stock.first().amount
