from decimal import Decimal
from typing import List

from django.db import models
from django.db.models import Sum


class BeverageManager(models.Manager):
    def get_sales_and_price_per_beverage(self) -> List[dict]:
        """Returns a list of dictionaries containing each beverages' id, name and all their prices."""
        return [
            {
                "name": e.name,
                "color": e.color,
                "prices": [
                    float(f.price) for f in e.stock_prices.all().order_by("timestamp")
                ],
            }
            for e in self.all()
        ]

    def get_total_retail_price(self) -> Decimal:
        """
        Returns the sum of all last stock_prices for each beverage
        """
        return self.aggregate(
            current_retail_price=Sum("retail_price"),
        )["current_retail_price"]

    def get_total_number_of_sales(self) -> Decimal:
        """
        Returns the sum of sales for each beverage
        """
        return self.aggregate(
            total_number_of_sales=Sum("number_of_sales"),
        )["total_number_of_sales"]
