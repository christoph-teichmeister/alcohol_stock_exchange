from django.urls import path

from .views import WarehouseListView

urlpatterns = [
    path("", WarehouseListView.as_view(), name="stocks"),
]
