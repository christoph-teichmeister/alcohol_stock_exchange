# Generated by Django 4.0.3 on 2022-03-27 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0006_alter_stockprice_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockprice',
            options={'ordering': ['-timestamp']},
        ),
    ]
