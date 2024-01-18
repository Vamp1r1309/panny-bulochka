from django.urls import path

from .views import basket_view, basket_add, basket_update, basket_delete, senMessageOrderInTelegram
app_name = 'basket'

urlpatterns = [
    path('<int:user_id>/', basket_view, name='basket-view'),
    path('add/<int:user_id>', basket_add, name='add-to-cart'),
    path('delete/<int:user_id>', basket_delete, name='delete-to-cart'),
    path('update/<int:user_id>', basket_update, name='update-to-cart'),
    path('sendMessage/<int:user_id>', senMessageOrderInTelegram, name='sendMessageTelegram'),
]