from django.urls import re_path

from market.consumers import MarketStatusConsumer

websocket_urlpatterns = [
    re_path(r"ws/market-status/", MarketStatusConsumer.as_asgi()),
]
