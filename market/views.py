from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from market.services import MarketChartContextService, ResetMarketService


def market_status(request):
    """
    Renders the market status.html template filled with each beverage's price data as initial context.
    The price data will be later updated via websockets.
    """
    return render(
        request=request,
        template_name="market/status.html",
        context={"data": MarketChartContextService.process()},
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
        TODO CT
        """

        ResetMarketService.process()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "market-status",
            {
                "type": "update_market_price_chart",
            },
        )

        return HttpResponse(200)
