# Generated by Django 4.0.3 on 2022-03-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverage', '0003_alter_beverage_options_beverage_number_of_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='beverage',
            name='retail_price',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=4),
            preserve_default=False,
        ),
    ]
