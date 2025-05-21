from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from app.database import Base
from datetime import date
from sqlalchemy.orm import relationship, mapped_column, Mapped

# class Bookings(Base):
#     __tablename__ = 'bookings'
#
#     # nullable=False - не пустой столбец
#     id = Column(Integer, primary_key=True)
#     room_id = Column(ForeignKey('rooms.id'))
#     user_id = Column(ForeignKey('users.id'))
#
#     date_from = Column(Date, nullable=False)
#     date_to = Column(Date, nullable=False)
#     price = Column(Integer)
#
#     total_cost = Column(Integer, Computed("(date_from - date_to) * price"))
#     total_days = Column(Integer, Computed("date_from - date_to"))

class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))