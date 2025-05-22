from app.database import async_session_maker
from sqlalchemy import select



class BaseDAO():
    model = None

    @classmethod
    async def find_by_id(cls, room_id):
        async with async_session_maker() as session:
            queue = select(cls.model).filter_by(id=room_id)
            result = await session.execute(queue)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            queue = select(cls.model).filter_by(**filter_by)
            result = await session.execute(queue)
            #спец метод в алхимии возвращающий один или none
            return result.scalar_one_or_none()


    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            queue = select(cls.model).filter_by(**filter_by)
            result = await session.execute(queue)
            return result.scalars().all()