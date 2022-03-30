from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from market.services import MarketHistoryChartContextService, ResetMarketService
from market.services.update_market_price_chart_ws_service import (
    UpdateMarketPriceChartWebsocketService,
)


def market_history(request):
    """
    Renders the market history.html template filled with each beverage's price data as initial context.
    The price data will be later updated via websockets.
    """
    return render(
        request=request,
        template_name="market/history.html",
        context={"data": MarketHistoryChartContextService.process()},
    )


class MarketControlView(generic.TemplateView):
    template_name = "market/control.html"
    http_method_names = [
        "get",  # for initial template loading
        "post",  # for reset_market method
    ]

    @staticmethod
    def reset_market(request, *args, **kwargs):
        """
        TODO CT: Comment
        """

        ResetMarketService.process()

        UpdateMarketPriceChartWebsocketService.process()

        return HttpResponse(200)
