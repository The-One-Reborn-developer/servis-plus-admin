from sqlalchemy import Integer, BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class SessionPlayers(Base):
    __tablename__ = 'session_players'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(Integer, nullable=False)
    player_telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    player_name: Mapped[str] = mapped_column(Text, nullable=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
