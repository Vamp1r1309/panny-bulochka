from django.urls import path
from api.views import index, show_category, show_posts, add_user_tg

app_name = 'api'

urlpatterns = [
    path('', index, name='home'),
    path('category/<slug:cat_slug>/',  show_category, name='category'),
    path('post/<slug:cat_slug>', show_posts, name='post'),
    path('register/', add_user_tg, name='reg')
]