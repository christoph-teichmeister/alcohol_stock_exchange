from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils import timezone

from beverage.models import Beverage
from stock_price.models import StockPrice


class RecalculatePricesService:
    @staticmethod
    def process(beverage: Beverage, revert_sale: bool):
        timestamp = timezone.now()

        new_beverage_price = (
            beverage.current_stock_price * (1 + beverage.price_weight)
            if not revert_sale
            else beverage.current_stock_price / (1 + beverage.price_weight)
        )

        # If a beverage is bought, its price should increase by * price_weight
        StockPrice.objects.create(
            price=new_beverage_price,
            beverage=beverage,
            timestamp=timestamp,
        )

        for other_beverage in Beverage.objects.exclude(id=beverage.id):
            # ALL other prices must then fall by their weight => price /= 100 * price_weight
            new_other_beverage_price = (
                other_beverage.current_stock_price * (1 + other_beverage.price_weight)
                if revert_sale
                else other_beverage.current_stock_price
                / (1 + other_beverage.price_weight)
            )

            StockPrice.objects.create(
                price=new_other_beverage_price,
                beverage=other_beverage,
                timestamp=timestamp,
            )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "market-status",
            {
                "type": "update_market_price_chart",
            },
        )
