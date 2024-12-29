from sqlalchemy import select

from app.database.models.bid import Bid
from app.database.models.sync_session import sync_session


async def get_bids(current_app, jsonify):
    try:
        with sync_session() as session:
            with session.begin():
                bids = session.scalars(select(Bid)).all()

        return jsonify(bids), 200
    except Exception as e:
        current_app.logger.error(f'Error fetching bids: {str(e)}')
        return jsonify({'error': str(e)}), 500