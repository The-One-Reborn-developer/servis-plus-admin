from sqlalchemy import Integer, BigInteger, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class Delivery(Base):
    __tablename__ = 'deliveries'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    customer_name: Mapped[str] = mapped_column(Text, nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    deliver_from: Mapped[str] = mapped_column(String(20), nullable=False)
    deliver_to: Mapped[str] = mapped_column(String(20), nullable=False)
    closed: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
