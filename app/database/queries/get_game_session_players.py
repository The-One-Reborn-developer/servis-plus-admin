from sqlalchemy import select

from app.database.models.session_players import SessionPlayers
from app.database.models.sync_session import sync_session


def get_game_session_players(session_id) -> int:
    with sync_session() as session:
        with session.begin():
            session_players = session.scalars(
                select(SessionPlayers).where(SessionPlayers.session_id == session_id)
            ).all()

            return [session_players.to_dict() for session_players in session_players]
