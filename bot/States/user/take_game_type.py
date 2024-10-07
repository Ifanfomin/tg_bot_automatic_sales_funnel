from aiogram.dispatcher.filters.state import State, StatesGroup


class WatchGamesListStates(StatesGroup):
    waiting_take_game_type = State()
    waiting_watch_games = State()
