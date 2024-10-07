from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.Utils.Database.requests import Database
from bot.Keyboards.common import user_menu_keyboard


async def cmd_menu(message: types.Message, role: str, db: Database , state: FSMContext):
    await state.finish()

    if role == "user":
        await message.answer("Вы вернулись в меню\n"
                             "Выберите одну из опций:", reply_markup=user_menu_keyboard()["keyboard"])
    elif role == "admin":
        ...