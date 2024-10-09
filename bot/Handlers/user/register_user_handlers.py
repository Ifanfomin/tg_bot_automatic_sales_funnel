from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from bot.Handlers.user.watch_games_list import take_game_type, start_watch_games_list, watch_next_game, watch_prev_game
from bot.States.user.take_game_type import WatchGamesListStates


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(take_game_type, Text(equals="Список игр", ignore_case=True), state="*")
    dp.register_callback_query_handler(start_watch_games_list, state=WatchGamesListStates.waiting_take_game_type)
    dp.register_callback_query_handler(watch_next_game, Text(equals="Следующая", ignore_case=True), state=WatchGamesListStates.waiting_watch_games)
    dp.register_callback_query_handler(watch_prev_game, Text(equals="Предыдущая", ignore_case=True), state=WatchGamesListStates.waiting_watch_games)
    dp.register_callback_query_handler(take_game_type, Text(equals="Категории", ignore_case=True), state=WatchGamesListStates.waiting_watch_games)

    # dp.register_message_handler(watch_next_game, state=WatchGamesListStates.waiting_watch_games)
    # dp.register_message_handler(watch_prev_game, state=WatchGamesListStates.waiting_watch_games)
