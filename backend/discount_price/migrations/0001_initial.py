# Generated by Django 4.2.1 on 2024-01-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('weight', models.CharField(blank=True, max_length=20, null='100г.', verbose_name='Вес')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/api/images/', verbose_name='Изображение товара')),
            ],
        ),
    ]