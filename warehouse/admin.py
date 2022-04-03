from django.contrib import admin

from warehouse.models import Stock


@admin.register(Stock)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "amount", "beverage"]
    readonly_fields = ["beverage"]


class StockInlineAdmin(admin.StackedInline):
    model = Stock
    extra = 0
