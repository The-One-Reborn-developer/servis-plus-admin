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

tables_blueprint = Blueprint(
    'tables',
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)


@tables_blueprint.get('/<service_name>')
def tables_for_service(service_name):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))
    
    try:
        pass
    except Exception as e:
        pass