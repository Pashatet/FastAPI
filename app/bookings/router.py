from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.bookings.models import Bookings

router = APIRouter(
    prefix='/bookings',
    #теги для документации
    tags=['Бронирование'],
)


@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        queue = select(Bookings)
        result = await session.execute(queue)
        return result.scalars().all()

# @router.get("/{booking_id}")
# def get_bookings_for_id(bookings_id):
#     pass