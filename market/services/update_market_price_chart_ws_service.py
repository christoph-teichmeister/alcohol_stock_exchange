from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class UpdateMarketPriceChartWebsocketService:
    @staticmethod
    def process():
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "market-status",
            {
                "type": "update_market_price_chart",
            },
        )
