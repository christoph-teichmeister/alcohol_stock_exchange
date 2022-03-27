from django.contrib import admin

from beverage.models import Beverage
from stock_price.admin import StockPriceInlineAdmin


@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    inlines = [
        StockPriceInlineAdmin,
    ]
