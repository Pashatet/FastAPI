from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.schemas import SBookings
from app.database import async_session_maker
from app.bookings.models import Bookings
from app.bookings.dao import BookingDAO


router = APIRouter(
    prefix='/bookings',
    #теги для документации
    tags=['Бронирование'],
)


@router.get("")
async def get_bookings() -> list[SBookings]:
    result = await BookingDAO.find_all( )
    return result
# @router.get("/{booking_id}")
# def get_bookings_for_id(bookings_id):
#     pass