# Generated by Django 4.0.3 on 2022-03-30 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverage', '0007_beverage_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='beverage',
            name='number_of_sales_before_price_falls_by_one_euro',
            field=models.DecimalField(decimal_places=2, default=1, help_text='Defines how many sales are made before the price has fallen by a full euro. Note: Price will fall before too! Think of it like the following mathematical function: f(x) = 1/{number_of_sales_before_price_falls_by_one_euro}x + {retail_price}.The price will hence never fall below the retail price but will slide along the linear graph.', max_digits=4),
        ),
    ]
