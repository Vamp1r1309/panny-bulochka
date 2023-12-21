from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

web_app = WebAppInfo(url="https://www.pannybulochka.ru/api/")
main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='знакомство'.upper(), web_app=web_app)
        ],
    ]
)

complite = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='yes'),
            InlineKeyboardButton(text='Нет', callback_data='no'),
        ]
    ]
)
