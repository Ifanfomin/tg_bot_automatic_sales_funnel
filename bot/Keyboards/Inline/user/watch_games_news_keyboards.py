from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def news_prev_next_keyboard():
    keyboard = InlineKeyboardMarkup()
    buttons = [
        "Предыдущая",
        "Меню",
        "Следующая"
    ]

    keyboard.add(
        *[InlineKeyboardButton(text=text, callback_data=text) for text in buttons]
    )

    return keyboard
