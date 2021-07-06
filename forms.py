from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, EqualTo, Length



class InputForm(Form):
    name = TextField(
        'Stop', validators=[DataRequired(), Length(min=2, max=25)]
    )




