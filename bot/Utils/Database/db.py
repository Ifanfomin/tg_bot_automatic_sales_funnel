# Подключение к базе данных PostgreSQL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Text
from sqlalchemy.orm import declarative_base, sessionmaker

from bot.config import config

host=config.DB_HOST
user=config.DB_USER
password=config.DB_PASS
database=config.DB_NAME
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:5432/{database}"

# Создание движка подключения
# engine = create_async_engine(DATABASE_URL)
engine = create_engine(DATABASE_URL)


metadata = MetaData()

users = Table("users", metadata,
    Column("user_id", Text(), primary_key=True),
    Column("username", Text()),
    Column("name", Text())
)

metadata.create_all(engine)


# Базовый класс для декларативных моделей
Base = declarative_base()

# session = async_sessionmaker(bind=engine)
session = sessionmaker(bind=engine)


