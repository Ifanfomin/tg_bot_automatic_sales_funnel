from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.Utils.Database.requests import Database
from bot.States.user.take_game_type import WatchGamesListStates
from bot.Keyboards.user import take_game_type_keyboard


async def show_game(message: types.Message, game_id: int, db: Database):
    game_info = await db.get_game_info(game_id)
    await message.answer_photo(
        photo=game_info[1],
        caption=f"<blockquote expandable>"
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
        parse_mode="HTML"
    )
    # await message.answer_photo(photo="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/262060/header.jpg", caption="<blockquote expandable>Окей\nЗдесь описание\nТо что ниже не видно\nхехехе\nтута остальная инфа</blockquote>", parse_mode="HTML")


async def take_game_type(message: types.Message, state: FSMContext):
    await state.set_state(WatchGamesListStates.waiting_take_game_type.state)

    await message.answer("Выбери интересующий жанр:", reply_markup=take_game_type_keyboard()["keyboard"])


async def start_watch_games_list(message: types.Message, db: Database, state: FSMContext):
    async with state.proxy() as data:
        if message.text in take_game_type_keyboard()["buttons"]:
            data["genre"] = message.text
            data["id_index"] = 0
            data["games_ids"] = await db.get_games_ids(data["genre"])
            await show_game(
                message,
                data["games_ids"][data["id_index"]],
                db
            )
        else:
            await message.answer("Выберите одну из опций", reply_markup=take_game_type_keyboard()["keyboard"])


# await message.answer_photo(photo="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/262060/header.jpg", caption="<blockquote expandable>Окей\nЗдесь описание\nТо что ниже не видно\nхехехе\nтута остальная инфа</blockquote>", parse_mode="HTML")

