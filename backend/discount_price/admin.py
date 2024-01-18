from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe

from discount_price.models import DiscountPrice


@admin.register(DiscountPrice)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'image_show', 'price')
    search_fields = ('name', 'price', 'cats',)
    list_filter = ('id', 'name')
    list_editable = ['price']
    empty_value_display = settings.EMPTY_MSG

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' height='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = 'Картинка'
