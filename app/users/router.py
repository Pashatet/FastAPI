from fastapi import APIRouter, HTTPException, status, Response, Depends

from .auth import get_password_hash, create_access_token, authenticate_user
from .dao import UserDAO
from .dependencies import get_current_user
from .models import Users
from .schemas import SUserAuth

# from app.exceptions import UserAl.readyExistsException
from app.bookings import schemas
from ..exeptions import *

router_auth = APIRouter(
    prefix="/auth",
    tags=["Авторизация пользователя"],
)

@router_auth.post("/register", status_code=201)
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    new_user = await UserDAO.add(email=user_data.email, hashed_password=hashed_password)


@router_auth.post("/login", status_code=200)
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    #значение любого ключа нужно проводить к строке
    access_token = create_access_token({'sub': str(user.id)})
    # сетим куку с нужным нам названием и httponly чтобы жто куку нельзя было достать через js
    response.set_cookie(key="booking_access_token", value=access_token, httponly=True)

    return access_token

@router_auth.post("/logout", status_code=200)
async def logout_user(response: Response):
    response.delete_cookie(key="booking_access_token")
    return 'Пользователь вышел из системы'

@router_auth.post("/me", status_code=200)
async def logout_user(current_user: Users = Depends(get_current_user)):
    return current_user

