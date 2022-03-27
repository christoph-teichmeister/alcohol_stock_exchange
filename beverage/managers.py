from decimal import Decimal
from typing import List

from django.db import models
from django.db.models import Sum


class BeverageManager(models.Manager):
    def get_sales_and_price_per_beverage(self) -> List[dict]:
        """Returns a list of dictionaries containing each beverages' id, name and all their prices."""
        return [
            {
                "id": e.id,
                "name": e.name,
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

    def calculate_beverage_price_weight(self) -> Decimal:
        sum_of_all_price_weights = Decimal(0)

        total_retail_price = self.get_total_retail_price()

        for beverage in self.all():
            beverage.price_weight = beverage.retail_price / total_retail_price
            sum_of_all_price_weights += beverage.price_weight
            beverage.save()

        return sum_of_all_price_weights
