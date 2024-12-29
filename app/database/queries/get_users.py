from sqlalchemy import select

from app.database.models.user import User
from app.database.models.sync_session import sync_session


def get_users(current_app, jsonify, service_name):
    fields = []
    
    if service_name == 'services':
        fields = [
            User.telegram_id,
            User.services_name,
            User.services_role,
            User.rate,
            User.experience,
            User.registered_in_services,
            User.services_registration_date
        ]
    elif service_name == 'delivery':
        fields = [
            User.telegram_id,
            User.delivery_name,
            User.delivery_role,
            User.date_of_birth,
            User.has_car,
            User.car_model,
            User.car_width,
            User.car_length,
            User.car_height,
            User.registered_in_delivery,
            User.delivery_registration_date
        ]
    
    try:
        with sync_session() as session:
            with session.begin():
                query = select(*fields).order_by(User.telegram_id)
                results = session.execute(query).all()

                users = [dict(row._mapping) for row in results]

        return users
    except Exception as e:
        current_app.logger.error(f'Error fetching users for service {service_name}: {str(e)}')
        return jsonify({'error': f'Error fetching users for service {service_name}: {str(e)}'}), 500