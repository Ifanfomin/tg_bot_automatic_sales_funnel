from aiogram.dispatcher.filters.state import State, StatesGroup


class WatchNewsListStates(StatesGroup):
    waiting_watch_news = State()
