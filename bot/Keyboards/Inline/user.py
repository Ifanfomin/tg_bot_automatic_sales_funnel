from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def take_game_type_keyboard():
    keyboard = InlineKeyboardMarkup()
    buttons = [
        "Топ популярных игр",
        "Головоломки",
        "Стратегии",
        "Рогалики",
        "Кооперативные",
        "Меню"
    ]

    keyboard.add(
        *[InlineKeyboardButton(text=text, callback_data=text) for text in buttons]
    )

    return keyboard


def game_prev_next_keyboard():
    keyboard = InlineKeyboardMarkup()
    buttons = [
        "Предыдущая",
        "Категории",
        "Следующая"
    ]

    keyboard.add(
        *[InlineKeyboardButton(text=text, callback_data=text) for text in buttons]
    )

    return keyboard
