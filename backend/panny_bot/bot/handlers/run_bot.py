from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from bot.utils import set_chat_menu_button
from bot.keyboards import main_kb


async def get_start(message: Message, bot: Bot):
    await set_chat_menu_button(bot)
    await message.answer(
        f"Привет, нам очень важно познакомиться с тобой, чтобы ты мог" 
        f"воспользоваться нашим подарком и получать самые горячие акции и предложения 🔥🔥",
        reply_markup=main_kb)