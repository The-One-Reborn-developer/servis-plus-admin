from sqlalchemy import select

from app.database.models.delivery import Delivery
from app.database.models.sync_session import sync_session


def get_deliveries(current_app, jsonify):
    try:
        with sync_session() as session:
            with session.begin():
                deliveries = session.scalars(select(Delivery)).all()

        return jsonify(deliveries), 200
    except Exception as e:
        current_app.logger.error(f'Error fetching deliveries: {str(e)}')
        return jsonify({'error': str(e)}), 500