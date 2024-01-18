from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse

from tg_users.models import UserTelegram

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
    
    # def get_absolute_url(self):
    #     return reverse('api:category', kwargs={"cat_slug": self.slug})


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
    quantity = models.PositiveIntegerField(default=1)
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

    # def get_absolute_url(self):
    #     return reverse('api:home', kwargs={"user_id": self.id})

    @property
    def full_image_url(self):
        """
        Returns:
            str: The full image URL.
        """
        return self.image.url if self.image else ''

    def __str__(self):
        return self.name


class ProductProxy(Catalog):

    objects = PublishedManager()

    class Meta:
        proxy = True