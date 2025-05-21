from typing import TYPE_CHECKING, Optional
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from app.database import Base
from sqlalchemy.orm import mapped_column, Mapped

# class Rooms(Base):
#     __tablename__ = 'rooms'
#
#     # nullable=False - не пустой столбец
#     id = Column(Integer, primary_key=True)
#     hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
#     name = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     price = Column(Integer, nullable=False)
#     services = Column(JSON, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     image_id = Column(Integer,)

class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]