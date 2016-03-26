from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/<string:name>')
def index(name):
    return render_template('auth/index.html', name=name)