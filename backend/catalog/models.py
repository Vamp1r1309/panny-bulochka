import random

from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from modules.services.utils import unique_slugify


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_published=Catalog.Status.PUBLISHED)


class Category(models.Model):
    name = models.CharField(
        'Категория',
        max_length=60,
        unique=True)
    slug = models.CharField(
        'Ссылка',
        max_length=100,
        unique=True,
        db_index=True,)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('api:category', kwargs={"cat_slug": self.slug})


# Create your models here.
class Catalog(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
    name = models.CharField(
        'Наименование',
        max_length=150,
        unique=True)
    description = models.TextField(
        'Описание товара',
        blank=True)
    weight = models.CharField(
        max_length=20,
        verbose_name='Вес',
        blank=True,
        null='100г.'
    )
    price = models.DecimalField(
        verbose_name='Цена',
        decimal_places=2,
        max_digits=10)
    image = models.ImageField(
        'Изображение товара',
        upload_to='static/api/images/',
        blank=True,
        null=True)
    cats = models.ManyToManyField(
        'Category',
        blank=True,
        verbose_name='Категория',
        related_name='posts'
    )
    time_create = models.DateTimeField(
        'Добавлен',
        auto_now_add=True)
    time_update = models.DateTimeField(
        'Изменён',
        auto_now=True)
    is_published = models.BooleanField(
        'Публикация',
        choices=Status.choices,
        default=Status.DRAFT)
    
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-time_create',)

    def __str__(self):
        return self.name


class UserTelegram(models.Model):
    """Пользовательский класс для хранения информации для пользователей"""

    telegram_id = models.CharField(
        'Телеграм ID',
        max_length=100,
        unique=True,
        default=random.randint(0, 100000)

    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
    )

    date_of_birth = models.DateField(
        'Дата рождения',
    )
    phone_user = models.CharField(
        'Номер телефона',
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)


    def __str__(self):
        return self.username


class Cart(models.Model):
    user = models.ForeignKey(UserTelegram, on_delete=models.CASCADE)
    product = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ('id',)

    def __str__(self) -> str:
        return f'Корзина для {self.user.user} | Продукт {self.product.name}'
