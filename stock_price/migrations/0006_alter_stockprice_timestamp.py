# Generated by Django 4.0.3 on 2022-03-27 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0005_stockprice_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Time at which this price has been issued'),
        ),
    ]
