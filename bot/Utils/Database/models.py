from bot.Utils.Database.db import Base

from typing import List, Optional
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str]
    name: Mapped[str]
    bought: Mapped[str]
    genres: Mapped[str]


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    image: Mapped[str]
    name: Mapped[str]
    developer: Mapped[str]
    price: Mapped[int]
    genre: Mapped[str]
    date: Mapped[str]
    alone: Mapped[str]
    koop: Mapped[str]
    description: Mapped[str]
    sysreq: Mapped[str]
    popularity: Mapped[int]

