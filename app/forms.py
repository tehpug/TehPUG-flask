from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):
    username = TextField('username', validators = [Required(), Length(min = 5, max = 50)])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class AddSessionForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 5, max = 100)])
	description = TextAreaField('description', validators = [Length(min = 0, max = 4000)])
	sound = TextField('sound')

class AddNewsForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 5, max= 100)])
	description = TextAreaField('description', validators = [Length(min = 0, max = 4000)])
	
		