from django.db import models
from catalog.models import UserTelegram, Catalog

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(UserTelegram, on_delete=models.CASCADE)
    product = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ('id',)

    def __str__(self) -> str:
        return f'Корзина для {self.user.user} | Продукты {self.product.name}'
