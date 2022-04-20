from decimal import Decimal

from django.utils import timezone

from core.helpers import get_stock_price_model, get_beverage_model
from market.services.update_market_price_chart_ws_service import (
    UpdateMarketPriceChartWebsocketService,
)

Beverage = get_beverage_model()
StockPrice = get_stock_price_model()


class RecalculatePricesService:
    def process(self, beverage: Beverage):
        timestamp = timezone.now()

        StockPrice.objects.create(
            price=self._get_new_price(beverage=beverage),
            beverage=beverage,
            timestamp=timestamp,
        )

        for other_beverage in Beverage.objects.exclude(id=beverage.id):
            StockPrice.objects.create(
                price=self._get_new_price(beverage=other_beverage),
                beverage=other_beverage,
                timestamp=timestamp,
            )

        UpdateMarketPriceChartWebsocketService.process()

    def _get_new_price(self, beverage: Beverage):
        return self._first_function(beverage)
        # return self._second_function(beverage)

    @staticmethod
    def _first_function(beverage: Beverage):
        """f(x) = 1/{number_of_sales_before_price_falls_by_one_euro}x + {retail_price}"""

        total_number_of_sales = Beverage.objects.get_total_number_of_sales()

        beverage_sales_vs_total_sales = Decimal(
            beverage.number_of_sales / total_number_of_sales
        )

        if beverage.number_of_sales == total_number_of_sales:
            beverage_sales_vs_total_sales = beverage.number_of_sales

        return (
            (1 / beverage.number_of_sales_before_price_falls_by_one_euro)
            * beverage_sales_vs_total_sales
        ) + (beverage.retail_price + 1)

    @staticmethod
    def _second_function(beverage: Beverage):
        """
        1/(1/4 * (X ′0.9)) + 4
        """
        total_number_of_sales = Beverage.objects.get_total_number_of_sales()

        beverage_sales_vs_total_sales = Decimal(
            beverage.number_of_sales / total_number_of_sales
        )

        if beverage.number_of_sales == total_number_of_sales:
            beverage_sales_vs_total_sales = beverage.number_of_sales

        if beverage_sales_vs_total_sales == 0:
            beverage_sales_vs_total_sales = 1

        if beverage.retail_price % 2 == 0:
            x1 = beverage.retail_price / 2
            x2 = x1
        else:
            x1 = beverage.retail_price / 2 + Decimal(0.5)
            x2 = beverage.retail_price - x1

        return (
            1 / (1 / x1 * Decimal(pow(beverage_sales_vs_total_sales, Decimal(0.9))))
            + x2
        )

    def _third_function(self):
        """
        Alle EKs zusammenrechnen => X
        Wenn Bier zu VK 2€ verkauft wird, muss der Bierpreis steigen.
        Dadurch hat Bier ein größeres Gewicht im Gesamtpreis X und die Differenz (X-Bierpreis) muss auf alle anderen
        Getränke zu einem Gewicht aufgeteilt werden.
        """
        pass

    def _fourth_function(self):
        """
        Ich fake das Angebot, indem ich sage, dass ich mir vorstelle, dass "Bier pro Minute = 5" verkauft wurde.
        Wenn die tatsächliche Nachfrage unter der Vorstellung liegt, sinkt der Preis, ansonsten steigt der.
        Das bräuchte einen Celery Task, der regelmäßig checkt, ob das so ist.

        Idee:
        Hier noch den Bestand einbringen in Relation zu Endzeit der Bar (das wäre ein neues Feld noch).
        Damit stünde am Anfang des Abends die Preisveränderung des Bieres bereits fest und ich habe eine Kurve,
        an der ich mich orientieren kann.
        """
        pass
