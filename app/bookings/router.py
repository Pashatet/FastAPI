from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.bookings.schemas import SBookings
from app.database import async_session_maker
from app.bookings.models import Bookings
from app.bookings.dao import BookingDAO
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    #теги для документации
    tags=['Бронирование'],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):  #-> list[SBookings]
    # print(user, type(user), user.email)
    # return user

    return await BookingDAO.find_all(user_id = 1)

# @router.get("/{booking_id}")
# def get_bookings_for_id(bookings_id):
#     pass