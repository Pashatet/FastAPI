from sqlalchemy import select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker


class BookingDAO(BaseDAO):
    model = Bookings


    # @classmethod
    # async def find_all(cls):
    #     async with async_session_maker() as session:
    #         queue = select(Bookings)
    #         result = await session.execute(queue)
    #         return result.scalars().all()

