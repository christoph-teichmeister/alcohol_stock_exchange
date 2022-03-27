from django.shortcuts import render

from market.services import MarketChartContextService


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
