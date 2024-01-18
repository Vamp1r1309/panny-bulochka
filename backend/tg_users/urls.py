from django.urls import path

from .views import add_user_tg

app_name = 'tg_users'

urlpatterns = [
    path('<int:chat_id>', add_user_tg, name='reg'),
]