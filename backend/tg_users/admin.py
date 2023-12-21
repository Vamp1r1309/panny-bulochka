from django.contrib import admin
from django.conf import settings

from .models import UserTelegram


@admin.register(UserTelegram)
class UserTelegramAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_user', 'time_create')
    search_fields = ('phone_user', 'username', 'time_create',)
    search_fields = ('name', 'phone_user',)
    empty_value_display = settings.EMPTY_MSG