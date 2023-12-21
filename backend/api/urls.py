from django.urls import path
from api.views import (index, show_category, 
                       show_posts)

app_name = 'api'

urlpatterns = [
    path('<int:chat_id>', index, name='home'),
    path('category/<slug:cat_slug>/',  show_category, name='category'),
    path('post/<slug:cat_slug>', show_posts, name='post'),
]