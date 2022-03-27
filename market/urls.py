from django.urls import path

from . import views
from .views import MarketControlView

urlpatterns = [
    path("status", views.market_status, name="market_status"),
    path("reset-market", MarketControlView.reset_market, name="reset_market"),
    path("controls", MarketControlView.as_view(), name="market_controls"),
]
