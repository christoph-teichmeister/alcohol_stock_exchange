from django.db import models


class BeverageManager(models.Manager):
    def sales_and_price_per_beverage(self):
        """Returns a list of dictionaries containing each beverages' id, name and all their prices."""
        return [
            {
                "id": e.id,
                "name": e.name,
                "prices": [float(f.price) for f in e.stock_prices.all()],
            }
            for e in self.all()
        ]
