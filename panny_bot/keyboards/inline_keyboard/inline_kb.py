from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

web_app = WebAppInfo(url="https://41f0-95-25-166-90.ngrok-free.app/register")
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
