from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from panny_bot.utils import set_chat_menu_button
from panny_bot.keyboards import main_kb
from panny_bot.config import db


async def get_start(message: Message, bot: Bot):
    await set_chat_menu_button(bot)
    # db_id = await db.check_chat_id(message.from_user.id)
    # print(db_id)
    # if not db_id:
    #     await message.answer("Вы уже зарегестрированы в нашей системе\nМожете посмотреть асортимент нашего магазина")
    # else:
    await message.answer(
        f"Привет, нам очень важно познакомиться с тобой, чтобы ты мог" 
        f"воспользоваться нашим подарком и получать самые горячие акции и предложения 🔥🔥",
        reply_markup=main_kb)