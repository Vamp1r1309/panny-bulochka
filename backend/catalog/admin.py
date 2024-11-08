from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings

from .models import Catalog, Category


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'image_show',
        'price', 'get_category', 'time_create',
        'time_update', 'weight', 'is_published',)
    search_fields = ('name', 'price', 'cats',)
    list_filter = ('id', 'cats')
    list_editable = ['price', 'weight']
    empty_value_display = settings.EMPTY_MSG

    @admin.display(description='Категории')
    def get_category(self, obj):
        return [cat.name for cat in obj.cats.all()]
    
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' height='60' />".format(obj.image.url))
        return "None"
    
    image_show.__name__ = 'Картинка'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug',)
    empty_value_display = settings.EMPTY_MSG
    prepopulated_fields = {'slug': ('name',)}
