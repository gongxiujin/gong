from itsdangerous import TimestampSigner
from flask import current_app

def get_jws_serializer():
    return TimestampSigner(current_app.config['SECRET_KEY'])


def verify_jws_token(token):
    s = get_jws_serializer()
    data = None
    invalid = False
    try:
        data = s.unsign(token, max_age=600)
    except Exception:
        invalid = True
    return invalid, data


def verify_auth_token(auth_token):
    invalid, data = verify_jws_token(auth_token)
    if invalid:
        return None
    loading_user = get_user(data[0])
    if loading_user \
            and data[1] == loading_user.password \
            and auth_token == loading_user.user_auth.access_token:
        return loading_user
    return None