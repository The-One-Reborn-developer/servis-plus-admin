from app.database.models.sync_session import sync_session
from app.database.models.game_session import GameSession


def insert_game_session(session_date, countdown_timer):
    with sync_session() as session:
        with session.begin():
            game_session = GameSession(
                session_date=session_date,
                countdown_timer=countdown_timer
            )
            session.add(game_session)
