from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.Services.Database.connecting import conn, cursor
from bot.bot import config_dict


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()

    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username
    cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        cursor.execute("INSERT INTO users (user_id, username, name) VALUES (%s, %s, %s)",
                       (user_id, user_name, user_full_name))
        conn.commit()

    if user_id in config_dict["ADMINS"]:











# async def cmd_start(message: types.Message, state: FSMContext):
#     await state.finish()
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton("/register"))
#     await message.answer(
#         "Привет! Нажми /register для регистрации",
#         reply_markup=keyboard
#     )