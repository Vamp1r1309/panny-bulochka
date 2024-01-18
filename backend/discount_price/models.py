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
    price = models.DecimalField(
        verbose_name='Цена',
        decimal_places=2,
        max_digits=10)
    image = models.ImageField(
        'Изображение товара',
        upload_to='static/api/images/',
        blank=True,
        null=True)