from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto

from bot.Keyboards.Inline.common import user_menu_keyboard


async def cmd_menu(call: types.CallbackQuery, role: str, state: FSMContext):
    await state.finish()

    if role == "user":
        photo = InputMediaPhoto(
            "https://github.com/Ifanfomin/tg_bot_automatic_sales_funnel/blob/master/imgs/widht_logo.jpg?raw=true")
        await call.message.edit_media(media=photo)
        await call.message.edit_caption(
            "Привет!\n"
                 "Здесь ты можешь покупать игры\n"
                 "Быть в курсе скидок\n"
                 "И игровых новостей!", reply_markup=user_menu_keyboard()
        )
    elif role == "admin":
        ...