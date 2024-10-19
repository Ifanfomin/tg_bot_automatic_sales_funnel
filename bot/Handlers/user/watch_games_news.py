from pyexpat.errors import messages

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto

from bot.Utils.Database.requests import Database
from bot.Utils.Parsers.ParseNews.parser import ParseNews
from bot.States.user.watch_news_states import WatchNewsListStates
from bot.Keyboards.Inline.user.watch_games_news_keyboards import news_prev_next_keyboard


async def show_news(call: types.CallbackQuery, news_info: dict):
    photo = InputMediaPhoto(news_info["img"])
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(
        f"{news_info['datetime']}\n"
        f"<b>{news_info['caption']}</b>\n"
        f"<a href=\"{news_info['url']}\">Ссылка на пост</a>",
        parse_mode="HTML",
        reply_markup=news_prev_next_keyboard()
    )


async def start_watch_games_news(call: types.CallbackQuery, news: ParseNews, state: FSMContext):
    await state.set_state(WatchNewsListStates.waiting_watch_news.state)

    async with state.proxy() as data:
        data["news_info"] = await news.get_news(0)
        data["news_num"] = 0
        await show_news(
            call,
            data["news_info"][data["news_num"]]
        )


async def watch_next_news(call: types.CallbackQuery, news: ParseNews, state: FSMContext):
    async with state.proxy() as data:
        data["news_num"] += 1
        print(data["news_num"])
        if data["news_num"] % 30 == 0:
            data["news_info"] = await news.get_news(data["news_num"])

        await show_news(
            call,
            data["news_info"][data["news_num"] % 30]
        )


async def watch_prev_news(call: types.CallbackQuery, news: ParseNews, state: FSMContext):
    async with state.proxy() as data:
        if data["news_num"] - 1 > -1:
            data["news_num"] -= 1
            print(data["news_num"])
            if data["news_num"] % 30 == 29:
                data["news_info"] = await news.get_news(data["news_num"])

        await show_news(
            call,
            data["news_info"][data["news_num"] % 30]
        )






