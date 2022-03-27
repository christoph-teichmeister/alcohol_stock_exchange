from django.db import models


class StockPrice(models.Model):
    price = models.DecimalField(default=1.00, max_digits=4, decimal_places=2)
    beverage = models.ForeignKey(
        "beverage.Beverage", related_name="stock_prices", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.price}€ : {self.beverage.name}"

    class Meta:
        ordering = [
            "-pk",
        ]
