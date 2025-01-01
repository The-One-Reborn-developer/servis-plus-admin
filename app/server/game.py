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


@game_blueprint.post('/add-game-session')
def add_game_session():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))

    session_date = request.form.get('session-date')

    print(session_date, type(session_date))