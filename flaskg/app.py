from flaskg.extensions import db, login_manager, bootstrap
from flask import Flask, render_template
from flaskg.auth.view import auth
import os, logging

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('flaskg.config.default.DefaultConfig')
    app.config.from_object(config)
    bootstrap.init_app(app)
    register_buleprint(app)
    error_hander(app)
    configure_logging(app)
    return app


def error_hander(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('auth/index.html')
# def configure_extensions(app):
#     with app.app_context():
#         @login_manager.request_loader
#         def load_user_from_request(http_request):
#             auth_header = http_request.headers.get('Authorization')
#             auth_header_prefix = 'Blue'
#             if auth_header:
#                 parts = auth_header.split()
#                 if len(parts) != 2 or parts[0].lower() != auth_header_prefix.lower():
#                     return None
#                 auth_token = parts[1]
#                 return verify_auth_token(auth_token)


def register_buleprint(app):
    app.register_blueprint(auth, url_prefix=app.config["AUTH_URL"])

def configure_logging(app):
    """Configures logging."""

    logs_folder = os.path.join(app.root_path, os.pardir, "logs")
    from logging.handlers import SMTPHandler

    pid_string = str(os.getpid())

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    info_log = os.path.join(logs_folder, app.config['INFO_LOG'] + '.' + pid_string)

    info_file_handler = logging.handlers.TimedRotatingFileHandler(info_log)

    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(formatter)
    app.logger.addHandler(info_file_handler)

    error_log = os.path.join(logs_folder, app.config['ERROR_LOG'] + '.' + pid_string)

    error_file_handler = logging.handlers.TimedRotatingFileHandler(error_log)

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)
