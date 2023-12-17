from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.cache import cache_page
from api.forms import AddRegisterUserForm
from catalog.models import Category, Catalog, UserTelegram



def index(request):
    post = Catalog.published.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'posts': post,
        'cat_selected': 0,
        'counter': 1
    }
    return render(request, 'api/index.html', context=data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Catalog.published.filter(cats__id=category.pk)
    data = {
        'menu': category,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'api/index.html', context=data)


def show_posts(request, cat_slug):
    post = Catalog.published.filter(cats__slug=cat_slug)
    data = {
        'menu': post,
        # 'cat_selected': post_tags,
    }
    return render(request, 'api/index.html', context=data)

def add_user_tg(request):
    print(request)
    if request.method == 'POST':
        form = AddRegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddRegisterUserForm()
    data = {
        'form': form
    }
    return render(request, 'api/forms/form.html', data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
