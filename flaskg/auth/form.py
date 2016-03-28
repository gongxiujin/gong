from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired, Optional

class NameForm(Form):
    name = StringField("what's your name?", validators=[DataRequired()])
    submit = SubmitField('save')
