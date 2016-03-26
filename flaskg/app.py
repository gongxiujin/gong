from flaskg.extensions import db, login_manager
from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('flaskg.config.default.DefaultConfig')
    app.config.from_object(config)


def configure_extensions(app):
    with app.app_context():
        @login_manager.request_loader
        def load_user_from_request(http_request):
            auth_header = http_request.headers.get('Authorization')
            auth_header_prefix = 'Blue'
            if auth_header:
                parts = auth_header.split()
                if len(parts) != 2 or parts[0].lower() != auth_header_prefix.lower():
                    return None
                auth_token = parts[1]
                return verify_auth_token(auth_token)
