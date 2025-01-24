from app.database.models.sync_session import sync_session
from app.database.models.game_session_ads import GameSessionAd


def insert_game_session_ad(session_id, ad_path):
    with sync_session() as session:
        with session.begin():
            game_session = GameSessionAd(
                session_id=session_id,
                ad_path=ad_path
            )
            session.add(game_session)
