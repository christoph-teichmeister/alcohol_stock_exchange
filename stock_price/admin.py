from django.contrib import admin

from stock_price.models import StockPrice


@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    pass


class StockPriceInlineAdmin(admin.StackedInline):
    model = StockPrice
    extra = 0
