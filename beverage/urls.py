from django.urls import path

from .views import BeverageListView, BeverageUpdateView

urlpatterns = [
    path("", BeverageListView.as_view(), name="beverages"),
    path("<int:pk>", BeverageUpdateView.as_view(), name="beverage"),
    path("<int:pk>/sold", BeverageUpdateView.sold, name="beverage_sold"),
    path(
        "<int:pk>/revert_sale",
        BeverageUpdateView.revert_sale,
        name="beverage_revert_sale",
    ),
]
