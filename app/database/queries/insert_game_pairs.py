import logging

from sqlalchemy import insert

from app.database.models.sync_session import sync_session
from app.database.models.game_pairs import GamePair


def insert_game_pairs(pairs, session_id):
    if not session_id:
        raise ValueError("session_id is required")
    with sync_session() as session:
        with session.begin():
            logging.info(f'Inserting {len(pairs)} game pairs for session {session_id}')
            session.execute(
                insert(GamePair),
                    [
                        {
                            'session_id': session_id,
                            'round': '1',
                            'player1_telegram_id': player1_telegram_id,
                            'player2_telegram_id': player2_telegram_id
                        } for player1_telegram_id, player2_telegram_id in pairs
                    ]
                )
