from django.views import generic

from warehouse.models import Stock


class WarehouseListView(generic.ListView):
    model = Stock
    context_object_name = "stocks"
    template_name = "warehouse/stock_list_base.html"

    def get_queryset(self):
        return super().get_queryset().select_related("beverage")
