from aiogram import Dispatcher

from bot.Handlers.common.start import cmd_start
from bot.Handlers.common.menu import cmd_menu


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_menu, commands="menu", state="*")
