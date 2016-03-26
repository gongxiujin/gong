from flaskg.extensions import db
import os


class DefaultConfig(object):
    _basedir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(
        os.path.dirname(__file__)))))
    DEBUG = False
    TESTING = False

    SEND_LOG = False

    INFO_LOG = 'access.log'
    ERROR_LOG = 'error.log'

    SQLALCHEMY_URI = "mysql://root:aima@localhost:3306/gong_db?charset=utf8mb4"

    SQLALCHEMY_ECHO = False

    WTF_CSRF_SECRET_KEY = 'donottellyou'

    LOGIN_VIEW = "auth.login"
    REAUTH_VIEW = "auth.reauth"
    LOGIN_MESSAGE_CATEGORY = "error"
    SECRET_KEY = '470cd86a9656c3e12afca890df438a22'