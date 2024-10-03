from bot.Utils.Database.db import Base

from typing import List, Optional
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str]
    name: Mapped[str]
