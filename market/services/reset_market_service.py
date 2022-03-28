import copy
from datetime import timedelta

from django.utils import timezone

from beverage.models import Beverage


class ResetMarketService:
    @staticmethod
    def process():
        """
        Resets stock_prices for each beverage.

        Iterates over each beverage, deletes excess prices, and creates two StockPrices with the same price.
        """
        now = timezone.now()
        now_in_one_second = now + timedelta(seconds=1)

        for beverage in Beverage.objects.all():
            beverage.number_of_sales = 0
            beverage.save()
            beverage_stock_prices = beverage.stock_prices.all()

            first_price = beverage_stock_prices.last()

            # Check if two or more prices for at least one beverage exist
            # If they do, reset all prices, so that only the first price exists
            if beverage_stock_prices.count() > 1:
                # Get all prices except the first price
                prices_to_be_deleted = beverage_stock_prices.exclude(id=first_price.id)
                # Delete all other prices
                prices_to_be_deleted.delete()

            # Duplicate first price per beverage (so that graph is started)
            second_price = copy.deepcopy(first_price)
            second_price.pk = None
            second_price.timestamp = now_in_one_second
            second_price.save()

            first_price.timestamp = now
            first_price.save()
