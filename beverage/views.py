from http.client import HTTPResponse

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Subquery, OuterRef
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import generic

from beverage.models import Beverage
from beverage.services import BeverageSaleService
from stock_price.models import StockPrice


class BeverageListView(generic.ListView):
    model = Beverage
    context_object_name = "beverages"
    template_name = "beverage/beverage_list.html"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related("stock_prices")
            .annotate(
                current_stock_price=Subquery(
                    StockPrice.objects.filter(beverage=OuterRef("pk")).values("price")
                )
            )
        )


class BeverageUpdateView(generic.UpdateView):
    model = Beverage
    fields = ["number_of_sales"]
    template_name = "beverage/beverage_list.html"

    @staticmethod
    def sold(request, *args, **kwargs):
        """
        Retrieves objects using the requests pk and increases its number_of_sales.
        Returns a render of beverage_card.html.
        """

        beverage = BeverageSaleService.process(beverage_id=kwargs.get("pk"))

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "market-status",
            {
                "type": "update_market",
            },
        )

        return render(
            request=request,
            template_name="beverage/beverage_card.html",
            context={"beverage": beverage},
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
            template_name="beverage/beverage_card.html",
            context={"beverage": beverage},
        )
