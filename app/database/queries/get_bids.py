from sqlalchemy import select

from app.database.models.bid import Bid
from app.database.models.sync_session import sync_session


def get_bids() -> list:
    with sync_session() as session:
        with session.begin():
            bids = session.scalars(select(Bid)).all()
            return [bid.to_dict() for bid in bids]
