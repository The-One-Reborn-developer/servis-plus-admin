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

from app.database.queries.post_game_session import post_game_session


load_dotenv(find_dotenv())
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)
TEMPLATES_DIR = f"{BASE_DIR}/web/templates"
STATIC_DIR = f"{BASE_DIR}/web/static"
ASSETS_DIR = f"{STATIC_DIR}/web/assets"

game_blueprint = Blueprint(
    'game',
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)


@game_blueprint.post('/add-session')
def add_session():
    try:
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))

        data = request.get_json()
        session_date = data.get('session_date')

        if not session_date:
            return jsonify({
                'error': 'Session date not provided',
                'message': 'Дата игровой сессии обязательна для заполнения.'
            }), 400

        game_session = post_game_session(session_date)
        return jsonify({
            'message': 'Игровая сессия успешно добавлена'
        }), 201
    except Exception as e:
        current_app.logger.error(f'Error adding game session: {str(e)}')
        return jsonify({
            'error': f'Error adding game session: {str(e)}'
        }), 500
