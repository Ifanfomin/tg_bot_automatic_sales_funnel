from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.Utils.Database.requests import Database
from bot.Keyboards.Inline.common import user_menu_keyboard


async def cmd_start(message: types.Message, role: str, db: Database , state: FSMContext):
    await state.finish()

    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username

    await db.add_user(
        user_id=str(user_id),
        username=user_name,
        name=user_full_name
    )

    if role == "user":
        await message.answer_photo(
            photo="https://github.com/Ifanfomin/tg_bot_automatic_sales_funnel/blob/master/imgs/widht_logo.jpg?raw=true",
            caption="Привет!\n"
                     "Здесь ты можешь покупать игры\n"
                     "Быть в курсе скидок\n"
                     "И игровых новостей!", reply_markup=user_menu_keyboard())
    elif role == "admin":
        ...

