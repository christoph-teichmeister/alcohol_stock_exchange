from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from market.services import MarketChartContextService


class MarketStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # self.room_group_name = f"chat_{self.room_name}"
        self.room_group_name = "market-status"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        """Leave room group"""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def update_market(self, *args, **kwargs):
        """Sends updated price data for the beverages to frontend"""

        # Get price data
        dict_data = await sync_to_async(MarketChartContextService.process)()

        # Send price_data to frontend
        await self.send(text_data=dict_data)
