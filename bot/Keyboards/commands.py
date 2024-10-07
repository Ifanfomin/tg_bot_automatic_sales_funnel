from aiogram import Bot
from aiogram.types import BotCommand


def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/menu", description="Вернуться в меню"),
        BotCommand(command="/profile", description="Посмотреть профиль"),
        BotCommand(command="/my_games", description="Посмотреть мои игры"),
        BotCommand(command="/list", description="Посмотреть список игр"),
        BotCommand(command="/register", description="Начать Регистрацию")
    ]

    bot.set_my_commands(commands)