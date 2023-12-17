# Generated by Django 4.2.1 on 2023-12-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_usertelegram_telegram_id_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('id',), 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterField(
            model_name='catalog',
            name='cats',
            field=models.ManyToManyField(blank=True, related_name='posts', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='telegram_id',
            field=models.CharField(default=18333, max_length=100, unique=True, verbose_name='Телеграм ID'),
        ),
    ]
