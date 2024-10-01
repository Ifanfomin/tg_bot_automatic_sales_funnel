from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import IDFilter
from bot.Services.Database.connecting import cursor


async def show_database(message: types.Message):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if users:
        response = "Список зарегистрированных пользователей:\n\n"
        for user in users:
            response += f"ID: {user[0]}\nИмя: {user[1]}\nТелефон: {user[2]}\nInstagram: {user[3]}\n\n"
        await message.answer(response, parse_mode=None)
    else:
        await message.answer("База данных пуста.")


def register_handlers_admin(dp: Dispatcher, ALLOWED_USER_IDS):
    dp.register_message_handler(show_database, IDFilter(user_id=""), commands="database", state="*")

