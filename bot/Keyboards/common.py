from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def user_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # , one_time_keyboard=True
    buttons = [
        "Список игр",
        "Игровые новости"
    ]
    keyboard.add(
        *[KeyboardButton(text) for text in buttons]
    )

    return {"keyboard": keyboard, "buttons": buttons}
