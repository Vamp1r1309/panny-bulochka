from django.contrib import admin
from .models import Basket
from django.conf import settings
# Register your models here.
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ('id', 'created_timestamp')
    empty_value_display = settings.EMPTY_MSG