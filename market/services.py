import json

from beverage.models import Beverage
from core.helpers import get_random_hex_code


class MarketChartContextService:
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
        all_sales_per_beverage = Beverage.objects.sales_and_price_per_beverage()

        return json.dumps(
            {
                "sales_per_beverage": all_sales_per_beverage,
                "color_config": [
                    {"id": beverage["id"], "color": get_random_hex_code()}
                    for beverage in all_sales_per_beverage
                ],
            }
        )
