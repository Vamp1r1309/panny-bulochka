from django.shortcuts import render, get_object_or_404
from catalog.models import Category, ProductProxy



def index(request, user_id):
    """
    Вывод главной страницы
    """
    post = ProductProxy.published.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'posts': post,
        'cat_selected': 0,
        'counter': 1,
        'user_id': user_id
        
    }
    return render(request, 'api/index.html', context=data)


def show_category(request, user_id, cat_slug):
    """
    Вывод товара по категориям
    """
    print(user_id, cat_slug)
    category = get_object_or_404(Category, slug=cat_slug)
    posts = ProductProxy.published.filter(cats__id=category.pk)
    data = {
        'menu': category,
        'posts': posts,
        'cat_selected': category.pk,
        'cat_slug': cat_slug,
        'user_id': user_id
    }
    return render(request, 'api/index.html', context=data)