# Generated by Django 4.2.1 on 2023-11-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_usertelegram_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertelegram',
            name='date_of_birth',
            field=models.CharField(max_length=10, unique=True, verbose_name='Дата рождения'),
        ),
    ]