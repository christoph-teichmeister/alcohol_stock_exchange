from beverage.models import Beverage


class BeverageSaleService:
    @staticmethod
    def process(beverage_id: int, revert_sale: bool = False):
        beverage = Beverage.objects.get(id=beverage_id)

        if revert_sale and beverage.number_of_sales <= 0:
            return ValueError

        beverage.number_of_sales += -1 if revert_sale else 1
        beverage.save()

        setattr(beverage, "current_stock_price", beverage.stock_prices.first().price)

        return beverage
