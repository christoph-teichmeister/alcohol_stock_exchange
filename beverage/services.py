from beverage.models import Beverage
from market.services import RecalculatePricesService


class BeverageSaleService:
    @staticmethod
    def process(beverage_id: int, revert_sale: bool = False):
        """Increases or decreases a beverages sales. Recalculates all prices accordingly."""
        beverage = Beverage.objects.get(id=beverage_id)

        if revert_sale and beverage.number_of_sales <= 0:
            return ValueError

        beverage.number_of_sales += -1 if revert_sale else 1
        beverage.save()

        RecalculatePricesService.process(beverage=beverage, revert_sale=revert_sale)

        return beverage
