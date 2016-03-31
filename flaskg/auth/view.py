from flask import Blueprint, render_template
from flaskg.auth.form import NameForm
from flaskg.auth.models import User, Role

auth = Blueprint('auth', __name__)

@auth.route('/<string:name>', methods=['GET', 'POST'])
def index(name):
    name_form = NameForm()
    if name_form.validate_on_submit():
        name = name_form.name.data
        user = User(name)
        user.save()
        Role('gong')
    return render_template('auth/index.html', name=name, form=name_form)