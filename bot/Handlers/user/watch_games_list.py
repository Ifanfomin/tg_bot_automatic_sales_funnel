from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto

from bot.Utils.Database.requests import Database
from bot.States.user.take_game_type import WatchGamesListStates
from bot.Keyboards.Inline.user import take_game_type_keyboard, game_prev_next_keyboard


async def take_game_type(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(WatchGamesListStates.waiting_take_game_type.state)

    photo = InputMediaPhoto("https://github.com/Ifanfomin/tg_bot_automatic_sales_funnel/blob/master/imgs/widht_logo.jpg?raw=true")
    await call.message.edit_media(media=photo)
    await call.message.edit_caption("Выбери интересующий жанр:", reply_markup=take_game_type_keyboard())


async def show_game(call: types.CallbackQuery, game_id: int, db: Database):
    game_info = await db.get_game_info(game_id)
    photo = InputMediaPhoto(game_info[1])
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(
        f"<blockquote expandable>"
            f"<b>Название</b>: {game_info[2]}\n"
            f"<b>Разработчик</b>: {game_info[3]}\n"
            f"<b>Цена</b>: {game_info[4]}\n"
            f"<b>Жанр</b>: {game_info[5]}\n"
            f"<b>Вышла</b>: {game_info[6]}\n"
            f"<b>Одиночный режим</b>: {game_info[7]}\n"
            f"<b>Кооператив</b>: {game_info[8]}\n"
            f"<b>Описание</b>: {game_info[9]}\n"
            f"<b>Минимальные требования</b>: {game_info[10]}\n"
            f"<b>Популярность</b>: {game_info[11]}"
            f"</blockquote>",
        parse_mode="HTML",
        reply_markup=game_prev_next_keyboard()
    )


async def watch_next_game(call: types.CallbackQuery, db: Database, state: FSMContext):
    async with state.proxy() as data:
        if data["id_index"] + 1 < len(data["games_ids"]):
            data["id_index"] += 1
            await show_game(
                call,
                data["games_ids"][data["id_index"]],
                db
            )


async def watch_prev_game(call: types.CallbackQuery, db: Database, state: FSMContext):
    async with state.proxy() as data:
        if data["id_index"] - 1 > -1:
            data["id_index"] -= 1
            await show_game(
                call,
                data["games_ids"][data["id_index"]],
                db
            )


async def start_watch_games_list(call: types.CallbackQuery, db: Database, state: FSMContext):
    await state.set_state(WatchGamesListStates.waiting_watch_games.state)

    async with state.proxy() as data:
        data["genre"] = call.data
        data["id_index"] = 0
        data["games_ids"] = await db.get_games_ids(data["genre"])
        await show_game(
            call,
            data["games_ids"][data["id_index"]],
            db
        )


# await message.answer_photo(photo="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/262060/header.jpg", caption="<blockquote expandable>Окей\nЗдесь описание\nТо что ниже не видно\nхехехе\nтута остальная инфа</blockquote>", parse_mode="HTML")

