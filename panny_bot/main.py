import asyncio
from aiogram import Bot, Dispatcher, F

from panny_bot.config import BOT_TOKEN
from panny_bot.utils import StateForm
from panny_bot.handlers import *
    

async def start():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.message.register(get_start, F.text == '/start')
    dp.callback_query.register(get_form, F.data == 'welcome')
    dp.message.register(get_form_year, StateForm.GET_NAME)
    dp.message.register(get_form_phone, StateForm.GET_YEAR)
    dp.message.register(end_form, StateForm.GET_PHONE)
    dp.callback_query.register(complite_cmd, F.data == 'yes')
    dp.callback_query.register(complite_error, F.data == 'no')
    try:
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"ERROR - {ex}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

