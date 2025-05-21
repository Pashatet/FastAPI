from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Hotels(Base):
    __tablename__ = 'hotels'


    # nullable=False - не пустой столбец
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[int] = mapped_column(nullable=False)
    #так как мы не вкурсе какие конеретно данные могут быть в json, тип его нужно указывать в mapped_column
    services: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    rooms_quantity: Mapped[int] = mapped_column(default=1, nullable=False)
    #если у нас пустой mapped_column его можно просто удалить
    image_id: Mapped[int]


# class Hotels(Base):
#     __tablename__ = 'hotels'
#
#
#     # nullable=False - не пустой столбец
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     location = Column(String, nullable=False)
#     services = Column(JSON, nullable=False)
#     rooms_quantity = Column(Integer, default=1, nullable=False)
#     image_id = Column(Integer)
