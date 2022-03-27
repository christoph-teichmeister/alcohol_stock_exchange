from datetime import timedelta
from decimal import Decimal
from typing import List

from django.db import models
from django.db.models import Sum


class StockPriceManager(models.Manager):
    def get_all_timestamps_as_list(self) -> List[str]:
        timestamp_values_list = self.all().values_list("timestamp", flat=True)

        distinct_timestamps = sorted(
            list(
                set(
                    [
                        timestamp.strftime("%H:%M:%S")
                        for timestamp in timestamp_values_list
                    ]
                )
            )
        )

        last_timestamp = timestamp_values_list.last()
        for minute_counter in range(1, 4):
            distinct_timestamps.append(
                (last_timestamp + timedelta(minutes=minute_counter)).strftime(
                    "%H:%M:%S"
                )
            )

        return distinct_timestamps

    def get_total_current_stock_price(self) -> Decimal:
        """
        Returns the sum of all last stock_prices for each beverage
        """
        last_timestamp = self.last().timestamp

        last_prices = self.filter(timestamp=last_timestamp)

        return last_prices.aggregate(
            current_total_stock_price=Sum("price"),
        )["current_total_stock_price"]
