from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from catalog.models import Category, Catalog
from tg_users.models import UserTelegram



def index(request, chat_id):
    """
    Вывод главной страницы
    """
    user = UserTelegram.objects.filter(id=chat_id)
    print(user)
    if not user:
        UserTelegram.objects.create(id=chat_id)
        
    
    post = Catalog.published.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'posts': post,
        'cat_selected': 0,
        'counter': 1
    }
    return render(request, 'api/index.html', context=data)


def show_category(request, cat_slug):
    """
    Вывод товара по категориям
    """
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Catalog.published.filter(cats__id=category.pk)
    data = {
        'menu': category,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'api/index.html', context=data)


def show_posts(request, cat_slug):
    """
    Показ опубликованных постов
    """
    post = Catalog.published.filter(cats__slug=cat_slug)
    data = {
        'menu': post,
    }
    return render(request, 'api/index.html', context=data)
