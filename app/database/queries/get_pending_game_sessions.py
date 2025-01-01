from sqlalchemy import select

from app.database.models.sync_session import sync_session
from app.database.models.game_session import GameSession


def get_pending_game_sessions():
    '''
    Get all sessions that are not started and not finished
    '''
    with sync_session() as session:
        with session.begin():
            game_sessions = session.scalars(select(GameSession).where(GameSession.started == False, GameSession.finished == False)).all()
            return [game_session.to_dict() for game_session in game_sessions]