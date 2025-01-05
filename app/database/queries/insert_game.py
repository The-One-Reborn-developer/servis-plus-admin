from app.database.models.sync_session import sync_session
from app.database.models.game import Game


def insert_game(session_id):
    with sync_session() as session:
        with session.begin():
            new_game = Game(
                session_id=session_id,
                round_number=1
            )
            session.add(new_game)
            session.flush()
            return new_game.id
