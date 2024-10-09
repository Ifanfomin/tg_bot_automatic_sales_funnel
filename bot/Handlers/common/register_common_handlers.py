from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from bot.Handlers.common.start import cmd_start
from bot.Handlers.common.menu import cmd_menu


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_callback_query_handler(cmd_menu, Text(equals="Меню", ignore_case=True), state="*")
