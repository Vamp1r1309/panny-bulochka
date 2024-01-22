import requests
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect


from .cart import Cart
from catalog.models import ProductProxy
from tg_users.models import UserTelegram

# Create your views here.

def basket_view(request, user_id):
    cart = Cart(request)
    context = {
        'cart': cart,
        'user_id': user_id,
    }
    return render(request, 'basket/basket-view.html', context)


def basket_add(request, user_id):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(ProductProxy, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_qty = cart.__len__()
        response = JsonResponse({'qty': cart_qty, 'product': product.name, 'user_id': user_id})

        return response
    print("Error")


def basket_delete(request, user_id):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_qty, 'total': cart_total, 'user_id': user_id})
        return response


def basket_update(request, user_id):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_qty, 'total': cart_total, 'user_id': user_id})
        return response


def sendMessageOrderInTelegram(request, user_id):
    cart = Cart(request)
    user = get_object_or_404(UserTelegram, id=user_id)
    messageInTGBOT = cart.sendMessage()
    URI_API = settings.URI_API
    params = {
        'chat_id': user_id,
        'text': messageInTGBOT,
        'parse_mode': 'html',

    }
    requests.get(URI_API, params=params)
    messageInTGBOT += f'Имя пользователя: <b>{user.username}</b>\nНомер телефона: <b>{user.phone_user}</b>'
    CHAT_ID = settings.CHAT_ID_ORDERS
    params = {
        'chat_id': CHAT_ID,
        'text': messageInTGBOT,
        'parse_mode': 'html',
    }

    requests.get(URI_API, params=params)
    cart.clean_users_session()
    message = "Ваш заказ успешно сформирован, ожидайте звонка оператора!Заказ в боте продублирован!Хорошего дня"
    context = {
	'cart': cart,
        'user_id': user_id,
	'message': message,
    }
    return render(request, 'basket/basket-view.html', context)
