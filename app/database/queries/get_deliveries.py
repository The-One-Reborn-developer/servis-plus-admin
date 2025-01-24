from sqlalchemy import select

from app.database.models.delivery import Delivery
from app.database.models.sync_session import sync_session


def get_deliveries() -> list:
    with sync_session() as session:
        with session.begin():
            deliveries = session.scalars(select(Delivery)).all()
            return [delivery.to_dict() for delivery in deliveries]
