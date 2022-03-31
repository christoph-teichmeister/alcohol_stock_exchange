from django.contrib import admin

from stock_price.models import StockPrice


@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ["__str__", "beverage", "price", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["beverage"]


class StockPriceInlineAdmin(admin.StackedInline):
    model = StockPrice
    extra = 0
