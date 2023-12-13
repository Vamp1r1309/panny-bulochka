from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, MenuButtonWebApp, WebAppInfo


# MenuButtonWebApp, WebAppInfo


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='cancel',
            description='Сбросить'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())

async def set_chat_menu_button(bot: Bot):
    menu_button = MenuButtonWebApp(
        type="web_app",
        text="Каталог",
        web_app=WebAppInfo(url='https://107d-95-25-158-183.ngrok-free.app/register/')
    )
    await bot.set_chat_menu_button(menu_button=menu_button)
