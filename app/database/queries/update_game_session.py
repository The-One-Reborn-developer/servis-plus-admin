import logging

from sqlalchemy import update

from app.database.models.game_session import GameSession
from app.database.models.sync_session import sync_session


def update_game_session(game_session_id, status, players_amount=None):
    if status not in ['started', 'finished']:
        raise ValueError('Invalid status')
    with sync_session() as session:
        with session.begin():
            if status == 'started':
                session.execute(update(GameSession).where(GameSession.id == game_session_id).values(started=True))
                logging.info(f"Game session {game_session_id} has been updated to {status}=True")
            elif status == 'finished':
                session.execute(update(GameSession).where(GameSession.id == game_session_id).values(finished=True,
                                                                                                    players_amount=players_amount))
                logging.info(f"Game session {game_session_id} has been updated to {status}=True and players_amount={players_amount}")
