# Generated by Django 4.0.3 on 2022-03-05 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("beverage", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="beverage",
            name="stock_prices",
        ),
    ]
