from sqlalchemy import Integer, BigInteger, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class Game(Base):
    __tablename__ = 'games'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    game_started: Mapped[bool] = mapped_column(Boolean, default=False)
    game_finished: Mapped[bool] = mapped_column(Boolean, default=False)
    round_number: Mapped[int] = mapped_column(Integer, nullable=False)
    winner_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=True)
    session_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

    def to_dict(self):
        return {c.name : getattr(self, c.name) for c in self.__table__.columns}
