from django.urls import path

from .views import basket_view
app_name = 'basket'

urlpatterns = [
    path('', basket_view, name='basket_vie')
]