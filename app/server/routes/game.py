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

from app.database.queries.insert_game_session import insert_game_session


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
        countdown_timer = data.get('countdown_timer')
        current_app.logger.info(f'Adding game session: {session_date}')
        if not session_date:
            return jsonify({
                'success': False,
                'message': 'Дата игровой сессии обязательна для заполнения.'
            }), 400

        insert_game_session(session_date, countdown_timer)
        return jsonify({
            'success': True,
            'message': 'Игровая сессия успешно добавлена'
        }), 201
    except Exception as e:
        current_app.logger.error(f'Error adding game session: {str(e)}', exc_info=True)
        return jsonify({
            'success': False,
            'message': 'Ошибка при добавлении игровой сессии'
        }), 500
