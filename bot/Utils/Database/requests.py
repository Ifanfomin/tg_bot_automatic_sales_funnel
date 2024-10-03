from os import write

from bot.Utils.Database.models import Users

# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy import delete, and_, select


class Database:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def add_user(self, user_id: str, username: str, name: str) -> None:
        # user = await self.session.get(Users, user_id)
        with self.session as session:
            query = select(Users).filter_by(user_id=user_id)
            user = session.execute(query).all()

            print(user)
            if not user:
                print("not user")
                user = Users(
                    user_id=user_id,
                    username=username,
                    name=name
                )
                session.add(user)
                session.commit()
