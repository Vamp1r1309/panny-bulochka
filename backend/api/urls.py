from django.urls import path
from api.views import (index, show_category)

app_name = 'api'

urlpatterns = [
    path('<int:user_id>/', index, name='home'),
    path('category/<int:user_id>/<str:cat_slug>/',  show_category, name='category'),
]