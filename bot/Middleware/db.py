from collections.abc import Callable
from typing import Dict, Any, Awaitable

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types.base import TelegramObject
from aiogram.types import Message
# from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from bot.Utils.Database.requests import Database


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session: sessionmaker[Session]):
        super(DatabaseMiddleware, self).__init__()
        self.session = session

    async def on_process_message(self, message: Message, data: Dict):
        with self.session() as session:
            db = Database(session=session)
            data["db"] = db
