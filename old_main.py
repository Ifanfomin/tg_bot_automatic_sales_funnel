import logging
import os
from dotenv import load_dotenv
import psycopg2
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


load_dotenv()

ALLOWED_USER_IDS = {}

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())
logging_middleware = LoggingMiddleware()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, name TEXT, phone TEXT, instagram TEXT)')
conn.commit()

class EditStates(StatesGroup):
    edit_name = State()
    edit_phone = State()
    edit_instagram = State()

class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_instagram = State()

def get_start_register_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("/register"))
    return keyboard

@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Нажми кнопку /register и расскажи о себе", reply_markup=get_start_register_keyboard())

@dp.message_handler(Command("register"))
async def register(message: types.Message):
    user_id = message.from_user.id
    cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        await message.answer("Ты уже зарегистрированы.")
    else:
        await message.answer("Проходя регистрацию ты даёшь согласие на обработку персональных данных")
        await message.answer("Как тебя зовут?")
        await RegistrationStates.waiting_for_name.set()

@dp.message_handler(state=RegistrationStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await message.answer("Введи номер телефона:")

    await RegistrationStates.waiting_for_phone.set()

@dp.message_handler(lambda message: not message.text.isdigit() or len(message.text) < 11, state=RegistrationStates.waiting_for_phone)
async def process_phone_invalid(message: types.Message):
    await message.reply("Не pizdи мне тут 🤭 – Введите корректный номер")

@dp.message_handler(lambda message: message.text.isdigit(), state=RegistrationStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        await message.answer("Введи никнейм Instagram:")

    await RegistrationStates.waiting_for_instagram.set()

@dp.message_handler(state=RegistrationStates.waiting_for_instagram)
async def process_instagram(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['instagram'] = message.text
        user_id = message.from_user.id
        name = data['name']
        phone = data['phone']
        instagram = data['instagram']
        cursor.execute("INSERT INTO users (user_id, name, phone, instagram) VALUES (%s, %s, %s, %s)",
                       (user_id, name, phone, instagram))
        conn.commit()

        await message.answer("Спасибо за регистрацию!")

    await state.finish()

    # Отправляем сообщение с ссылкой и кнопкой
    await bot.send_message(user_id, "Бегом смотри", reply_markup=get_link_keyboard())
    await bot.send_message(user_id, "Чтобы обсудить детали, нажми на кнопку  — «С кем связаться?»")

# Функция для создания кнопки "С кем связаться?"
def get_link_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("С кем связаться?"))
    return keyboard


@dp.message_handler(lambda message: message.text == "С кем связаться?")
async def contact_me(message: types.Message):
    await message.answer("")


@dp.message_handler(Command("bd"), user_id=ALLOWED_USER_IDS)
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




@dp.message_handler(Command("edit_name"))
async def edit_name_start(message: types.Message):
    await message.answer("Введи новое имя для редактирования:")
    await EditStates.edit_name.set()

@dp.message_handler(state=EditStates.edit_name)
async def edit_name_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        user_id = message.from_user.id
        new_name = data['name']
        cursor.execute("UPDATE users SET name=%s WHERE user_id=%s", (new_name, user_id))
        conn.commit()
        await message.answer("Имя успешно обновлено.")
    await state.finish()

@dp.message_handler(Command("edit_phone"))
async def edit_phone_start(message: types.Message):
    await message.answer("Введи новый номер телефона для редактирования:")
    await EditStates.edit_phone.set()

@dp.message_handler(state=EditStates.edit_phone)
async def edit_phone_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        user_id = message.from_user.id
        new_phone = data['phone']
        cursor.execute("UPDATE users SET phone=%s WHERE user_id=%s", (new_phone, user_id))
        conn.commit()
        await message.answer("Номер телефона успешно обновлен.")
    await state.finish()

@dp.message_handler(Command("edit_instagram"))
async def edit_instagram_start(message: types.Message):
    await message.answer("Введи новый никнейм Instagram для редактирования:")
    await EditStates.edit_instagram.set()

@dp.message_handler(state=EditStates.edit_instagram)
async def edit_instagram_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['instagram'] = message.text
        user_id = message.from_user.id
        new_instagram = data['instagram']
        cursor.execute("UPDATE users SET instagram=%s WHERE user_id=%s", (new_instagram, user_id))
        conn.commit()
        await message.answer("Никнейм Instagram успешно обновлен.")
    await state.finish()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
