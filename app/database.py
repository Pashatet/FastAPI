from sqlalchemy import MetaData, inspect
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, as_declarative

from app.config import settings


# DB_HOST = 'localhost'
# DB_PORT = '5433'
# DB_USER = 'admin'
# DB_PASS = 'edarub73'
# DB_NAME = 'myhotels'

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL)

#expire_on_commit=False - при исполнении транзакции мы можем дальше работать с бд. ГЕНЕРАТОР СЕССИЙ
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

"""используется для миграций. Base в этом классе будут аккумулироваться данные о всех этих моделях,
чтобы затем алембик мог сравнить наше состояние на беке и в бд"""
class Base(DeclarativeBase):
    pass