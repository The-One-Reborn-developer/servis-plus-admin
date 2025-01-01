from app.database.models.game_session import GameSession
from app.database.models.sync_session import sync_session


def post_game_session(session_date):
    with sync_session() as session:
        with session.begin():
            game_session = GameSession(session_date=session_date)
            session.add(game_session)
