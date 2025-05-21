from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from app.database import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped

# class Users(Base):
#     __tablename__ = 'users'
#
#     # nullable=False - не пустой столбец
#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False)
#     hashed_password = Column(String, nullable=False)

# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]