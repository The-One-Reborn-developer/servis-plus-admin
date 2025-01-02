from sqlalchemy import select

from app.database.models.game_session import GameSession
from app.database.models.sync_session import sync_session


def get_game_session(session_id: int) -> dict:
    with sync_session() as session:
        with session.begin():
            game_session = session.scalar(select(GameSession).where(GameSession.id == session_id))
            
            if not game_session:
                return None
            
            return game_session.to_dict()
