from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Required, Length
import os

class RegisterForm(Form):
	username = TextField('username', validators = [Required(), Length(min = 4, max = 50)])
	password = PasswordField('password', validators = [Required(), Length(min = 4, max = 50)])
	email = TextField('email', validators = [Required(), Length(min = 6, max = 50)])


class LoginForm(Form):
    username = TextField('username', validators = [Required(), Length(min = 4, max = 50)])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class AddSessionForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 5, max = 100)])
	description = TextAreaField('description', validators = [Length(min = 0, max = 4000)])
	sound = SelectField('sound',choices = [])

class AddNewsForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 5, max= 100)])
	description = TextAreaField('description', validators = [Length(min = 0, max = 4000)])
	
