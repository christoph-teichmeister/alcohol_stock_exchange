from django.contrib import admin

from beverage.models import Beverage
from stock_price.admin import StockPriceInlineAdmin
from warehouse.admin import StockInlineAdmin


@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    inlines = [
        StockInlineAdmin,
        StockPriceInlineAdmin,
    ]
    list_display = ["name", "retail_price", "number_of_sales"]
