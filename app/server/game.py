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
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))

    session_date = request.form.get('session-date')
    current_app.logger.info(f'session_date: {session_date}')
    return jsonify({
        'session_date': session_date,
        'type': str(type(session_date))
    }), 200
