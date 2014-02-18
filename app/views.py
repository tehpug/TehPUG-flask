from flask import render_template, request
from werkzeug import secure_filename
import os
#from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app

###-------------------Base and Menu----------------###
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/tehpug')
def tehpug():
	return render_template('tehpug.html')

@app.route('/sessions')
def sessions():
	return render_template('sessions.html')

@app.route('/news')
def news():
	return render_template('news.html')

@app.route('/list')
def list():
	return render_template('list.html')

@app.route('/irc')
def irc():
	return render_template('irc.html')

###-------------Control Panel and logins-----------###
@app.route('/login')
def login():
	return render_template('login.html')

#@login_required
@app.route('/cpanel')
def cpanel():
	return render_template('cpanel.html')

#@login_required
@app.route('/files', methods = ['GET', 'POST','DELETE'])
def files():
	if request.method == 'POST':
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join('app/static/uploaded',filename))
	if request.method == 'DELETE':
		print (request.id)
	files = os.listdir('app/static/uploaded')
	return render_template('files.html', files = files)

###--------------Errors Handeling------------------###
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404