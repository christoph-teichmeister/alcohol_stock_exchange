# Generated by Django 4.0.3 on 2022-03-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverage', '0008_beverage_number_of_sales_before_price_falls_by_one_euro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beverage',
            name='price_weight',
        ),
        migrations.AlterField(
            model_name='beverage',
            name='number_of_sales_before_price_falls_by_one_euro',
            field=models.DecimalField(decimal_places=2, default=1, help_text="Defines how many sales are made before the price has fallen by a full euro. \nNote: Price will fall before this number is reached too! \nThink of it like the following mathematical function: \nf(x) = 1/{number_of_sales_before_price_falls_by_one_euro}x + {retail_price} \nwhere 'x' is the beverages number_of_sales / total_sales. \nThe price will hence never fall below the retail price but will slide along the linear graph.", max_digits=4),
        ),
    ]
