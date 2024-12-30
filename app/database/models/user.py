from sqlalchemy import Integer, BigInteger, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    services_role: Mapped[str] = mapped_column(String(20), nullable=True)
    delivery_role: Mapped[str] = mapped_column(String(20), nullable=True)
    services_name: Mapped[str] = mapped_column(Text, nullable=True)
    delivery_name: Mapped[str] = mapped_column(Text, nullable=True)
    rate: Mapped[int] = mapped_column(Integer, nullable=True)
    experience: Mapped[int] = mapped_column(Integer, nullable=True)
    date_of_birth: Mapped[str] = mapped_column(String(20), nullable=True)
    has_car: Mapped[bool] = mapped_column(Boolean, nullable=True)
    car_model: Mapped[str] = mapped_column(Text, nullable=True)
    car_width: Mapped[int] = mapped_column(Integer, nullable=True)
    car_length: Mapped[int] = mapped_column(Integer, nullable=True)
    car_height: Mapped[int] = mapped_column(Integer, nullable=True)
    registered_in_services: Mapped[bool] = mapped_column(Boolean, default=False)
    registered_in_delivery: Mapped[bool] = mapped_column(Boolean, default=False)
    services_registration_date: Mapped[str] = mapped_column(String(20), nullable=True)
    delivery_registration_date: Mapped[str] = mapped_column(String(20), nullable=True)