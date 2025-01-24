from sqlalchemy import Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class GamePair(Base):
    __tablename__ = 'game_pairs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(Integer, nullable=False)
    round: Mapped[str] = mapped_column(Integer, nullable=False)
    player1_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    player2_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    player1_choice: Mapped[str] = mapped_column(Integer, nullable=True)
    player2_choice: Mapped[str] = mapped_column(Integer, nullable=True)
    winner_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
