from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def user_menu_keyboard():
    keyboard = InlineKeyboardMarkup()
    buttons = [
        "Список игр",
        "Игровые новости"
    ]
    keyboard.add(
        *[InlineKeyboardButton(text=text, callback_data=text) for text in buttons]
    )

    return keyboard
