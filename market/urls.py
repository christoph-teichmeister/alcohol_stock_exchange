from django.urls import path

from . import views
from .views import MarketControlView

urlpatterns = [
    path("history", views.market_history, name="market_history"),
    path("reset-market", MarketControlView.reset_market, name="reset_market"),
    path("controls", MarketControlView.as_view(), name="market_controls"),
]
