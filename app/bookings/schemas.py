from pydantic import BaseModel
from datetime import date


class SBookings(BaseModel):

    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int


    #смотри к нашему классу не как на словарь а еще как к классу у которого есть атрибуты
    class Config:
        orm_mode = True