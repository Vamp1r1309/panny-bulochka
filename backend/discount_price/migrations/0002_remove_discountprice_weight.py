# Generated by Django 4.2.1 on 2024-01-18 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discount_price', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountprice',
            name='weight',
        ),
    ]
