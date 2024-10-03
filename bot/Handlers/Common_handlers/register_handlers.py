from aiogram import Dispatcher

from bot.Handlers.Common_handlers.start import (
    cmd_start,
    # cmd_menu
)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    # dp.register_message_handler(cmd_menu, commands="menu", state="*")
