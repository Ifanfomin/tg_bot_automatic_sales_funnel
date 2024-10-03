import logging
from aiogram import executor
from bot.bot import dp  # Импортируем уже настроенный диспетчер из bot.py

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Основная функция для запуска бота
async def on_startup(dispatcher):
    logging.info("Бот запущен и готов к работе.")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, on_startup=on_startup)
