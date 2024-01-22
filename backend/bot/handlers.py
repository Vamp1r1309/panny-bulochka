from aiogram import Bot
from aiogram.types import CallbackQuery, Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from bot.utils import set_commands


async def get_start(message: Message, bot: Bot):
    await set_commands(bot)
    print(message.from_user.id)
    print(type(message.from_user.id))
    web_app_register = WebAppInfo(url=f"https://www.pannybulochka.ru/register/{message.chat.id}")
    main_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='знакомство'.upper(), web_app=web_app_register)
            ],
        ]
    )
    await message.answer(
        f"Привет, нам очень важно познакомиться с тобой, чтобы ты мог"
        f"воспользоваться нашим подарком и получать самые горячие акции и предложения 🔥🔥",
        reply_markup=main_kb)


async def get_about(message: Message, bot: Bot):
    await message.answer('Кондитерская Пани Булочка уже год радует своими десертами жителей г. Краснодар\n'
                         'Пани Булочка - это\n'
                         '✨ натуральные ингредиенты и качественные продукты\n'
                         '✨ кондитерская в центре Краснодара\n'
                         '✨ авторские начинки и дегустационные сеты\n✨ индивидуальный подход к каждому клиенту\n'
                         '✨ внимательные менеджеры, которые всегда на связи, чтобы помочь вам сделать заказ\n'
                         '✨ команда профессиональных кондитеров, любящих свое дело.\nМы находимся по адресу: '
                         '<b>г. Краснодар, ул. Буденного, 125</b>.\nБудем ждать тебя в гости, чтобы познакомиться '
                         'лично 💕'
                         )


async def get_call_about(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    await callback.message.answer('Кондитерская Пани Булочка уже год радует своими десертами жителей г. Краснодар\n'
                                  'Пани Булочка - это\n'
                                  '✨ натуральные ингредиенты и качественные продукты\n'
                                  '✨ кондитерская в центре Краснодара\n'
                                  '✨ авторские начинки и дегустационные сеты\n✨ индивидуальный подход к каждому '
                                  'клиенту\n'
                                  '✨ внимательные менеджеры, которые всегда на связи, чтобы помочь вам сделать заказ\n'
                                  '✨ команда профессиональных кондитеров, любящих свое дело.\nМы находимся по адресу: '
                                  '<b>г. Краснодар, ул. Буденного, 125</b>.\nБудем ждать тебя в гости, '
                                  'чтобы познакомиться лично 💕'
                                  )


async def get_help(message: Message, bot: Bot):
    await message.answer(
        f"Привет, мы всегда рады вам помочь\n"
        f"Напишите нам с какими проблемами вы столкнулись и мы постораемся решить их в ближайшее время")


async def get_call_help(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    await callback.message.answer(
        f"Привет, мы всегда рады вам помочь\n"
        f"Напишите нам с какими проблемами вы столкнулись и мы постораемся решить их в ближайшее время")


async def enter_bonus_and_enter_menu(callback: CallbackQuery, bot: Bot):
    web_app_menu = WebAppInfo(url=f"https://www.pannybulochka.ru/api/{callback.message.chat.id}")
    main_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Меню'.upper(), web_app=web_app_menu),
            ],
            [
                InlineKeyboardButton(text='О нас', callback_data='call_about'),
                InlineKeyboardButton(text='Помощь', callback_data='call_help'),
            ],
        ]
    )
    await callback.message.answer('РАЗОВАЯ СКИДКА 30% НА ЗАКАЗ ИЛИ ПОКУПКУ В КОНДИТЕРСКОЙ ПАНИ БУЛОЧКА')
    await callback.message.answer('мы рады приветствовать тебя в сообществе кондитерской Пани Булочка. '
                                  'Теперь ты будешь в числе самых первых получать все самые горячие акции, скидки и '
                                  'знакомится с нашими новинками.'
                                  'Присоединяйся к нашему сообществу в телеграм-канале: https://t.me/+sNGfZOAkO51mODdi',
                                  reply_markup=main_kb)


