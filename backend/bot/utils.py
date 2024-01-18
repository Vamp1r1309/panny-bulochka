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
            command='about',
            description='О нас'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())