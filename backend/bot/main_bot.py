from aiogram import Bot, types, Dispatcher, F
from django.conf import settings

from bot.handlers import (enter_bonus_and_enter_menu, get_start,
                          get_about, get_help, get_call_help,
                          get_call_about)


async def start():
    bot = Bot(token=settings.BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.callback_query.register(enter_bonus_and_enter_menu, F.data == 'surprise')
    dp.callback_query.register(get_call_about, F.data == 'call_about')
    dp.callback_query.register(get_call_help, F.data == 'call_help')
    dp.message.register(get_start, F.text == '/start')
    dp.message.register(get_about, F.text == '/about')
    dp.message.register(get_help, F.text == '/help')
    try:
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"ERROR - {ex}")
    finally:
        await bot.session.close()