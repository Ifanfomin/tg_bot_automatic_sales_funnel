from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def take_game_type_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # , one_time_keyboard=True
    buttons = [
        "Топ популярных игр",
        "Головоломки",
        "Стратегии",
        "Рогалики",
        "Кооперативные",
        "Меню"
    ]

    keyboard.add(
        *[KeyboardButton(text) for text in buttons]
    )

    return {"keyboard": keyboard, "buttons": buttons}


def game_list_search_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Предыдущая",
        "Категории",
        "Следующая"
    ]
    keyboard.add(
        *[KeyboardButton(text) for text in buttons]
    )

    return {"keyboard": keyboard, "buttons": buttons}
