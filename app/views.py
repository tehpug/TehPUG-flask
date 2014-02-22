from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm, AddSessionForm
from models import User, Session
from hashlib import sha256
import os

###-------------Control Panel and logins-----------###
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('cpanel'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		user = User.query.filter_by(username = form.username.data).first()
		if user:
			if user.password == sha256(form.password.data).hexdigest():
				remember_me = False
    			if 'remember_me' in session:
        			remember_me = session['remember_me']
        			session.pop('remember_me', None)
				login_user(user, remember = remember_me)
	return render_template('login.html', form = form)


@app.route('/cpanel')
@login_required
def cpanel():
	return render_template('cpanel.html')

@app.route('/cpanel/sessions', methods = ['GET', 'POST', 'DELETE'])
@login_required
def cpanel_sessions():
	form = AddSessionForm()
	if form.validate_on_submit():
		session = Session(
			title = form.title.data,
			description = form.description.data,
			sound = form.sound.data,
			user_id = g.user.id)
		db.session.add(session)
		db.session.commit()
	sessions = Session.query.all()
	return render_template('cpanel_sessions.html', form = form, sessions = sessions)

@app.route('/cpanel/news', methods = ['GET', 'POST', 'DELETE'])
@login_required
def cpanel_news():
	return render_template('cpanel_news.html')

@app.route('/cpanel/files', methods = ['GET', 'POST','DELETE'])
@login_required
def files():
	if request.method == 'POST':
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join('app/static/uploaded',filename))
	if request.method == 'DELETE':
		pass
		#Delete the selected file
	files = os.listdir('app/static/uploaded')
	return render_template('files.html', files = files)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

###-------------------Base and Menu----------------###
@app.route('/')
@app.route('/index')
def index():
	sessions = Session.query.all()
	sessions.reverse()
	return render_template('index.html', sessions = sessions[:5])

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

###--------------Errors Handeling------------------###
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404