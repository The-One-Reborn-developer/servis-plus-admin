import logging

from sqlalchemy import select

from app.database.models.sync_session import sync_session
from app.database.models.game_session import GameSession


def get_pending_game_sessions() -> list:
    '''
    Get all sessions that are not started and not finished
    or started but not finished
    '''
    with sync_session() as session:
        with session.begin():
            game_sessions = session.scalars(
                select(GameSession).where((GameSession.finished == False))).all()

            logging.info(f"Found {len(game_sessions)} pending game sessions")
            for game_session in game_sessions:
                logging.info(f"Session ID: {game_session.id}, Session Date: {game_session.session_date}, Started: {game_session.started}, Finished: {game_session.finished}")

            return [game_session.to_dict() for game_session in game_sessions]
