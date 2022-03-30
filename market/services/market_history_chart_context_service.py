import json

from core.helpers import get_beverage_model, get_stock_price_model

Beverage = get_beverage_model()
StockPrice = get_stock_price_model()


class MarketHistoryChartContextService:
    @staticmethod
    def process():
        """
        Returns a json.dumped dictionary containing sales_per_beverage and color_config

        sales_per_beverage
            Result of Beverage.objects.sales_and_price_per_beverage().
            Is a list of dictionaries consisting of a beverages' id, name and all its prices.

        color_config
            Is a list of dictionaries containing each beverages' id and a random generated hex_code.
        """
        all_sales_per_beverage = Beverage.objects.get_sales_and_price_per_beverage()
        all_timestamps = StockPrice.objects.get_all_timestamps_as_list()

        temp = json.dumps(
            {
                "sales_per_beverage": all_sales_per_beverage,
                "all_timestamps": all_timestamps,
            }
        )

        # For easy breakpoints
        return temp
