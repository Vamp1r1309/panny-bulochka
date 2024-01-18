from django import template
from catalog.models import Category
from django.shortcuts import get_object_or_404


register = template.Library()

@register.inclusion_tag('api/includes/list_categories.html')
def show_categories(user_id, cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected, 'user_id': user_id}
