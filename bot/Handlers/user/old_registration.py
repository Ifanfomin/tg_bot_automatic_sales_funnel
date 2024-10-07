from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from bot.Services.Database.connecting import cursor, conn



class EditStates(StatesGroup):
    edit_name = State()
    edit_phone = State()
    edit_instagram = State()

class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_instagram = State()


async def registration_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        await message.answer("Ты уже зарегистрированы.")
        await state.finish()
    else:
        await message.answer("Проходя регистрацию ты даёшь согласие на обработку персональных данных")
        await message.answer("Как тебя зовут?")
        await state.set_state(RegistrationStates.waiting_for_name.state)


async def registration_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await state.set_state(RegistrationStates.waiting_for_phone.state)
    await message.answer("Введи номер телефона:")

async def registration_phone(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or len(message.text) < 11:
        await message.reply("Введи пожалуйста корректный номер")
        return

    async with state.proxy() as data:
        data['phone'] = message.text

    await state.set_state(RegistrationStates.waiting_for_instagram.state)
    await message.answer("Введи ник Instagram:")

async def registration_instagram(message: types.Message, state: FSMContext):
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


def register_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(registration_start, commands="register", state="*")
    dp.register_message_handler(registration_name, state=RegistrationStates.waiting_for_name)
    dp.register_message_handler(registration_phone, state=RegistrationStates.waiting_for_phone)
    dp.register_message_handler(registration_instagram, state=RegistrationStates.waiting_for_instagram)
