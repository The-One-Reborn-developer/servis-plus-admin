from sqlalchemy import select

from app.database.models.game_session import GameSession
from app.database.models.sync_session import sync_session


def get_game_sessions() -> list:
    with sync_session() as session:
        with session.begin():
            game_sessions = session.scalars(select(GameSession)).all()
            return [game_session.to_dict() for game_session in game_sessions]
