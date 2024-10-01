import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.middlewares.environment import EnvironmentMiddleware

from bot.Services.commands import set_commands
from bot.config import config
from bot.Middleware.role_middleware import RoleMiddleware

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Мидлварь для логирования
dp.middleware.setup(LoggingMiddleware())

# Преобразование конфигурации в словарь
config_dict = {
    "BOT_TOKEN": config.BOT_TOKEN,
    "ADMINS": config.admins_list,  # Используйте преобразованный список
    "ASSISTANTS": config.assistants_list,  # Используйте преобразованный список
    "SUPER_USERS": config.SUPER_USERS,
    "DB_HOST": config.DB_HOST,
    "DB_USER": config.DB_USER,
    "DB_PASS": config.DB_PASS,
    "DB_NAME": config.DB_NAME
}

# Мидлварь для управления окружением (передача конфигурации как словарь)
dp.middleware.setup(EnvironmentMiddleware(config_dict))

# Мидлварь для проверки ролей (админ, ассистент, пользователь)
# dp.middleware.setup(RoleMiddleware())

# Создание меню команд
set_commands(bot)

# Регистрация хендлеров
from bot.Handlers import User_handlers, Assistant_handlers, Admin_handlers, Common_handlers

# Common_handlers.register_handlers(dp)
# Assistant_handlers.register_handlers_task_creation(dp)