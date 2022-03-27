from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("<str:room_name>/", views.room, name="room"),
    path("status", views.market_status, name="market-status"),
]
