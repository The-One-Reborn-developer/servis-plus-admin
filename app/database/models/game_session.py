from sqlalchemy import Integer, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class GameSession(Base):
    __tablename__ = 'game_sessions'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_date: Mapped[str] = mapped_column(Text, nullable=False)
    players_amount: Mapped[int] = mapped_column(Integer, nullable=True)
    countdown_timer: Mapped[int] = mapped_column(Integer, nullable=False)
    started: Mapped[bool] = mapped_column(Boolean, default=False)
    finished: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
