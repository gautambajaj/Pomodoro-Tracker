from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, StringField

class LoginForm(FlaskForm):
	username = TextField('username')
	password = PasswordField('password')