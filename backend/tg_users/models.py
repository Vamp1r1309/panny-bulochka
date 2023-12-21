from django.db import models

# Create your models here.
class UserTelegram(models.Model):
    """Пользовательский класс для хранения информации для пользователей"""
    id = models.BigIntegerField(
        'Telegram id',
        primary_key=True,
        unique=True
    )

    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        null=True,
    )

    date_of_birth = models.DateField(
        'Дата рождения',
        null=True
    )
    phone_user = models.CharField(
        'Номер телефона',
        max_length=100,
        unique=True,
        null=True
    )
    time_create = models.DateTimeField(
        'Зарегистрирован',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)


    def __str__(self):
        if self.username is None:
            return str(self.id)
        return self.username