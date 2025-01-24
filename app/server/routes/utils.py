import os

from dotenv import (
    load_dotenv,
    find_dotenv
)

from werkzeug.utils import secure_filename

from flask import (
    Blueprint,
    current_app,
    request,
    jsonify
)

from app.database.queries.insert_game_session_ad import insert_game_session_ad


load_dotenv(find_dotenv())
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ADS_UPLOAD_DIR = os.path.join(PROJECT_ROOT, 'videos', 'ads')
ALLOWED_EXTENSIONS = {'mp4', 'mkv', 'mov', 'avi', 'wmv'}


utils_blueprint = Blueprint(
    'utils',
    __name__
)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@utils_blueprint.post('/upload-video')
def upload_video():
    if 'video-url' not in request.files:
        return jsonify({
            'success': False,
            'message': 'Файл не прикреплен'
        }), 400
    
    file = request.files['video-url']

    if file.filename == '':
        return jsonify({
            'success': False,
            'message': 'Файл не выбран'
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            'success': False,
            'message': 'Недопустимый тип файла'
        }), 400

    session_id = request.form.get('game-session-id')
    filename = secure_filename(file.filename)
    filepath = os.path.join(ADS_UPLOAD_DIR, filename)
    public_path = f'/videos/ads/{filename}'

    try:
        file.save(filepath)
        insert_game_session_ad(session_id, public_path)
        return jsonify({
            'success': True,
            'message': 'Видео успешно загружено',
            'filepath': filepath
        })
    except Exception as e:
        current_app.logger.error(f'Error uploading video: {str(e)}', exc_info=True)
        return jsonify({
            'success': False,
            'message': 'Ошибка при загрузке видео'
        }), 500
