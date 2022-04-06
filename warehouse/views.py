from django.views import generic

from warehouse.models import Stock


class WarehouseListView(generic.ListView):
    model = Stock
    context_object_name = "stocks"
    template_name = "warehouse/stock_list_base.html"

    def get_queryset(self):
        return super().get_queryset().select_related("beverage")

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     stocks_dict_list = [e.__dict__ for e in self.model.objects.all()]
    #     return {
    #         **super().get_context_data(object_list=object_list, **kwargs),
    #         "stocks_dict_list": stocks_dict_list,
    #     }
