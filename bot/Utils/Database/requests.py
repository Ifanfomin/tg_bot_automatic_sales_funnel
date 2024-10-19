from requests import session

from bot.Utils.Database.models import User, Game
from bot.Utils.Database.db import users, games

from sqlalchemy.orm import Session
from sqlalchemy import select


class Database:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def add_user(self, user_id: str, username: str, name: str) -> None:
        with self.session as session:
            query = select(users).filter_by(user_id=user_id)
            user = session.execute(query).all()

            print(user)
            if not user:
                print("not user")
                user = User(
                    user_id=user_id,
                    username=username,
                    name=name
                )
                session.add(user)
                session.commit()

    async def get_games_ids(
            self,
            genre: str
    ):
        with self.session as session:
            if genre == "Топ популярных игр":
                query = select(Game.id, Game.popularity)
                ls = session.execute(query).all()
                print(ls)
                ls = sorted(ls, key=lambda x: x[1], reverse=True)
                print(ls)
                ids = [d[0] for d in ls]
            else:
                query = select(Game.id).filter_by(genre=genre)
                ids = session.execute(query).all()
                ids = [i[0] for i in ids]
            print("ids", ids)
            return ids

    async def get_game_info(
            self,
            id: int
    ):
        with self.session as session:
            query = select(games).filter_by(id=id)
            game_info = session.execute(query).one()

            return game_info
    
    async def get_news_ids(self):
        with self.session as session:
            query = select(News.id)
            ids = session.execute(query).all()
            ids = [i[0] for i in ids]

            return ids
