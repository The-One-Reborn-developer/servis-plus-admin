import os

from dotenv import (
    load_dotenv,
    find_dotenv
)

from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
    url_for,
    redirect,
    session,
    flash
)


load_dotenv(find_dotenv())
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)
TEMPLATES_DIR = f"{BASE_DIR}/web/templates"
STATIC_DIR = f"{BASE_DIR}/web/static"
ASSETS_DIR = f"{STATIC_DIR}/web/assets"

admin_blueprint = Blueprint(
    'admin',
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)


@admin_blueprint.route('/')
def login():
    return render_template('login.html')


@admin_blueprint.post('/login')
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == os.getenv('USERNAME') and password == os.getenv('PASSWORD'):
        session['admin_logged_in'] = True
        return redirect(url_for('admin.dashboard'))
    else:
        flash('Неправильный логин или пароль', 'error')
        current_app.logger.error(f'Failed login attempt for user: {username} with password: {password}')
        return redirect(url_for('admin.login'))
    

@admin_blueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
