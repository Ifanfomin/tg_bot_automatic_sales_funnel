from typing import Dict

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from sqlalchemy.orm import sessionmaker, Session

from bot.Utils.Parsers.ParseNews.parser import ParseNews


class ParseNewsMiddleware(BaseMiddleware):
    def __init__(self):
        super(ParseNewsMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: Dict):
            news = ParseNews()
            data["news"] = news

    async def on_process_callback_query(self, call: types.CallbackQuery, data: Dict):
        news = ParseNews()
        data["news"] = news
