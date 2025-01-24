from flask import (
    Blueprint,
    current_app,
    request,
    url_for,
    redirect,
    session,
    jsonify
)

from app.database.queries.get_users import get_users
from app.database.queries.get_bids import get_bids
from app.database.queries.get_deliveries import get_deliveries
from app.database.queries.get_game_sessions import get_game_sessions


tables_blueprint = Blueprint(
    'tables',
    __name__
)


@tables_blueprint.get('/tables')
def tables_for_service():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))

    service_name = request.args.get('service')

    if not service_name:
        return jsonify({'error': 'Service name not provided'}), 400
    
    try:
        service_tables = {
            'services': ['Пользователи', 'Заказы'],
            'delivery': ['Пользователи', 'Доставки'],
            'game': ['Игровые сессии'],
            'ads': ['Материалы для игровой сессии']
        }

        tables = service_tables.get(service_name, [])

        if not tables:
            return jsonify({'error': f'No tables available for service {service_name}'}), 400
        
        return jsonify([{'name': table} for table in tables]), 200
    except Exception as e:
        current_app.logger.error(f'Error fetching tables for service {service_name}: {str(e)}')
        return jsonify({
            'error': f'Error fetching tables for service {service_name}: {str(e)}'
        }), 500


@tables_blueprint.get('/table')
def table_data():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))

    service_name = request.args.get('service')
    table_name = request.args.get('table')

    if not service_name or not table_name:
        return jsonify({
            'success': False,
            'message': 'Необходимо указать имя сервиса и имя таблицы'   
        }), 400

    try:
        if table_name == 'Пользователи':
            data = get_users(service_name)
        elif table_name == 'Заказы':
            data = get_bids()
        elif table_name == 'Доставки':
            data = get_deliveries()
        elif table_name == 'Игровые сессии':
            data = get_game_sessions()
        else:
            return jsonify({
                'success': False,
                'message': 'Таблица не найдена'
            }), 400

        return jsonify(data), 200
    except ValueError as ve:
        current_app.logger.error(f'Validation error for table {table_name}: {str(ve)}')
        return jsonify({
            'success': False,
            'message': 'Ошибка валидации'
        }), 400
    except Exception as e:
        current_app.logger.error(f'Error fetching data for table {table_name}: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'Ошибка при получении данных'
        }), 500
