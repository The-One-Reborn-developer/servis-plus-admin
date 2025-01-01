import logging

from sqlalchemy import update

from app.database.models.game_session import GameSession
from app.database.models.sync_session import sync_session


def update_game_session(game_session_id, status):
    if status not in ['started', 'finished']:
        raise ValueError('Invalid status')
    with sync_session() as session:
        with session.begin():
            if status == 'started':
                session.execute(update(GameSession).where(GameSession.id == game_session_id).values(started=True))
            elif status == 'finished':
                session.execute(update(GameSession).where(GameSession.id == game_session_id).values(finished=True))

            logging.info(f"Game session {game_session_id} has been updated to {status}=True")