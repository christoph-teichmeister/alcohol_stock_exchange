from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import generic

from beverage.models import Beverage
from beverage.services import BeverageSaleService


class BeverageListView(generic.ListView):
    model = Beverage
    context_object_name = "beverages"
    template_name = "beverage/beverage_list_base.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("stock_prices")


class BeverageUpdateView(generic.UpdateView):
    model = Beverage
    fields = ["number_of_sales"]

    @staticmethod
    def sold(request, *args, **kwargs):
        """
        Retrieves objects using the requests pk and increases its number_of_sales.
        Returns a render of beverage_card.html.
        """

        BeverageSaleService.process(beverage_id=kwargs.get("pk"))

        return render(
            request=request,
            template_name="beverage/beverage_list.html",
            context={
                "beverages": Beverage.objects.all().prefetch_related("stock_prices"),
            },
        )

    @staticmethod
    def revert_sale(request, *args, **kwargs):
        """
        Retrieves objects using the requests pk and increases its number_of_sales.
        Returns a render of beverage_card.html.
        """
        beverage = BeverageSaleService.process(
            beverage_id=kwargs.get("pk"), revert_sale=True
        )

        if beverage == ValueError:
            return HttpResponseBadRequest()

        return render(
            request=request,
            template_name="beverage/beverage_list.html",
            context={
                "beverages": Beverage.objects.all().prefetch_related("stock_prices"),
            },
        )
