import os

from dotenv import (
    load_dotenv,
    find_dotenv
)

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


load_dotenv(find_dotenv())
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)
TEMPLATES_DIR = f"{BASE_DIR}/web/templates"
STATIC_DIR = f"{BASE_DIR}/web/static"
ASSETS_DIR = f"{STATIC_DIR}/web/assets"

tables_blueprint = Blueprint(
    'tables',
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
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
            'delivery': ['Пользователи', 'Доставки']
        }

        tables = service_tables.get(service_name, [])

        if not tables:
            return jsonify({'error': f'No tables available for service {service_name}'}), 400
        
        return jsonify([{'name': table} for table in tables]), 200
    except Exception as e:
        current_app.logger.error(f'Error fetching tables for service {service_name}: {str(e)}')
        return jsonify({'error': f'Error fetching tables for service {service_name}: {str(e)}'}), 500


@tables_blueprint.get('/table')
def table_data():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))

    service_name = request.args.get('service')
    table_name = request.args.get('table')

    if not service_name or not table_name:
        return jsonify({'error': 'Service name or table name not provided'}), 400

    try:
        if table_name == 'Пользователи':
            data = get_users(service_name)
        elif table_name == 'Заказы':
            data = get_bids()
        elif table_name == 'Доставки':
            data = get_deliveries()
        else:
            return jsonify({'error': f'Invalid table name provided: {table_name}'}), 400

        return jsonify(data), 200
    except ValueError as ve:
        current_app.logger.error(f'Validation error for table {table_name}: {str(ve)}')
        return jsonify({'error': f'Validation error for table {table_name}: {str(ve)}'}), 400
    except Exception as e:
        current_app.logger.error(f'Error fetching data for table {table_name}: {str(e)}')
        return jsonify({'error': f'Error fetching data for table {table_name}: {str(e)}'}), 500
