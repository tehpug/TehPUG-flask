from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Required, Length
import os

sounds = []
files = os.listdir('app/static/uploaded')
for f in files:
	sounds += [(f,f)]

class LoginForm(Form):
    username = TextField('username', validators = [Required(), Length(min = 5, max = 50)])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class AddSessionForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 5, max = 100)])
	description = TextAreaField('description', validators = [Length(min = 0, max = 4000)])
	sound = SelectField('sound',choices = sounds)

class AddNewsForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 5, max= 100)])
	description = TextAreaField('description', validators = [Length(min = 0, max = 4000)])
	
