from sqlalchemy import insert

from app.database.models.sync_session import sync_session
from app.database.models.game_pairs import GamePair


def insert_game_pairs(pairs):
    with sync_session() as session:
        with session.begin():
            session.execute(
                insert(GamePair),
                    [
                        {
                            'game_id': game_id,
                            'player1_telegram_id': player1_telegram_id,
                            'player2_telegram_id': player2_telegram_id
                        } for game_id, player1_telegram_id, player2_telegram_id in pairs
                    ]
                )
