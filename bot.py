import asyncio
import logging
import os
from dotenv import load_dotenv

from app.handlers.common import register_handlers_common
from app.handlers.registration import register_handlers_registration
from app.handlers.admin import register_handlers_admin

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv()
logger = logging.getLogger(__name__)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/register", description="Начать Регистрацию")
    ]

    await bot.set_my_commands(commands)


async def main():
    # Делаем логирование
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logger.error("Starting bot")

    # Делаем бота и диспетчер
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрация хендлеров
    register_handlers_common(dp)
    register_handlers_registration(dp)
    register_handlers_admin(dp, os.getenv("ALLOWED_USER_IDS"))

    # Установка комманд бота
    await set_commands(bot)

    # Начинаем пуллить
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())



