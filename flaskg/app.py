from flaskg.extensions import db, login_manager, bootstrap
from flask import Flask, render_template
from flaskg.auth.view import auth

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('flaskg.config.default.DefaultConfig')
    app.config.from_object(config)
    bootstrap.init_app(app)
    register_buleprint(app)
    error_hander(app)
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