from django.contrib import admin, messages

from beverage.models import Beverage
from stock_price.admin import StockPriceInlineAdmin


@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    actions = ["recalculate_all_price_weights"]
    inlines = [
        StockPriceInlineAdmin,
    ]
    list_display = ["name", "retail_price", "price_weight"]

    def recalculate_all_price_weights(self, request, queryset):
        self.message_user(
            request=request,
            message="Your selection was ignored - ALL price-weights have been calculated",
            level=messages.WARNING,
        )
        sum_of_all_price_weights = Beverage.objects.calculate_beverage_price_weight()
        self.message_user(
            request=request,
            message=f"Sum of all price_weights is: {sum_of_all_price_weights}",
            level=messages.INFO,
        )
