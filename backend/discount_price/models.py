from django.db import models


# Create your models here.
class DiscountPrice(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=150,
        unique=True)
    description = models.TextField(
        'Описание товара',
        blank=True)
    price = models.CharField(
        verbose_name='Цена',
        max_length=20,
        blank=True)
    image = models.ImageField(
        'Изображение товара',
        upload_to='static/api/images/',
        blank=True,
        null=True)
