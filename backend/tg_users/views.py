from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import json

from api.forms import AddRegisterUserForm
from bot.inline_keyboard import btn_surprise

import requests


def add_user_tg(request, chat_id: int):
    """
    Добавления пользователя в модель UserTelegram
    """
    if request.method == 'POST':
        user_forms = request.POST.copy()
        user_forms['id'] = chat_id
        form = AddRegisterUserForm(user_forms)
        if form.is_valid():
            form.save()
            TOKEN = settings.BOT_TOKEN
            CHAT_ID = settings.CHAT_ID_REGISTRATIONS

            message = f"<b>Регистрация пользователя!</b>\nИмя пользователя: <b>{user_forms['username']}</b>\nНомер телефона: <b>{user_forms['phone_user']}</b>\nДата рождения: <b>{user_forms['date_of_birth']}</b>"
            URI_API = f"https://api.telegram.org/bot{TOKEN}/sendMessage?"

            params = {
                'chat_id': CHAT_ID,
                'text': message,
                'parse_mode': 'html'

            }
            messages.success(request, 'Ваш аккаунт создан!Возвращайтесь в бота для получения скидки!')
            requests.get(URI_API, params=params)

            params = {
                'chat_id': chat_id,
                'text': 'Теперь ты будешь в числе самых первых получать все самые горячие акции, скидки и знакомится с нашими новинками.Также здесь ты можешь узнать информацию о нас ознакомиться с меню и сделать заказ. \nЗАБИРАЙ СВОЙ ПОДАРОК 👇🏻',
                'reply_markup': json.dumps(btn_surprise)
                 
            }
            print(requests.get(URI_API, params=params))
            return redirect(f'/register/{chat_id}')
    else:
        form = AddRegisterUserForm()
    data = {
        'form': form,
        'chat_id': chat_id,
    }
    return render(request, 'tg_users/forms/form.html', data)