from django.db import models

from beverage.managers import BeverageManager


class Beverage(models.Model):
    name = models.CharField(max_length=50)
    number_of_sales = models.IntegerField(default=0)

    objects = BeverageManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "name",
        ]
