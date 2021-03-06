# Generated by Django 4.0.3 on 2022-03-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverage', '0005_alter_beverage_retail_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='beverage',
            name='price_weight',
            field=models.DecimalField(decimal_places=2, default=0.5, help_text='Price-Weight - calculated by dividing the sum of all prices by the beverages retail_price', max_digits=4),
            preserve_default=False,
        ),
    ]
