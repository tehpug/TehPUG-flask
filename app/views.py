from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug import secure_filename
from app import app, db, lm
from forms import LoginForm, AddSessionForm, AddNewsForm, RegisterForm 
from models import User, Session, News
from hashlib import sha256
import os
from datetime import datetime
###-------------Register and logins--------------###
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(
			username = form.username.data, 
			password = sha256(form.password.data).hexdigest(),
			email = form.email.data)
		db.session.add(user)
		db.session.commit()
		#verification email and login
		redirect(url_for('index'))
	return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	print form.validate_on_submit()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user:
			if user.password == sha256(form.password.data).hexdigest():
				login_user(user, remember = form.remember_me.data)
	if g.user is not None and g.user.is_authenticated() and g.user.admin:
		return redirect(request.args.get('next') or url_for('cpanel'))
	if g.user is not None and g.user.is_authenticated() and  not g.user.admin:
		return redirect(request.args.get('next') or url_for('user/'+g.user.username))
	return render_template('login.html', form = form)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

###-------------------User Profile-----------------###
@app.route('/user/<username>', methods = ['GET', 'POST'])
@login_required
def function(username):
	user = User.query.filter_by(username = username).first()
	if g.user.username == username:
		return render_template('Profile.html', user = user)
	else:
		return render_template('user.html', user = user)

###----------------------Cpanel--------------------###
@app.route('/cpanel')
@login_required
def cpanel():
	if g.user.admin:
		return render_template('cpanel.html')
	else:
		return render_template('access_err.html')

@app.route('/cpanel/sessions', methods = ['GET', 'POST'])
@app.route('/cpanel/sessions/<id>', methods = ['GET', 'POST', 'DELETE'])
@login_required
def cpanel_sessions(id = None):
	if g.user.admin:
		if request.method == 'DELETE' and id:
			db.session.delete(Session.query.get(id))
			db.session.commit()
		form = AddSessionForm()
		sounds = []
		files = os.listdir('app/static/uploaded')
		for f in files:
			sounds += [(f,f)]
		form.sound.choices = sounds
		if request.method == 'GET' and id:
			session = Session.query.get(int(id))
			form.title.data = session.title
			form.description.data = session.description
			form.sound.data = session.sound
		if request.method == 'POST' and id and form.validate_on_submit():
			session = Session.query.get(int(id))
			session.title = form.title.data
			session.description = form.description.data
			session.sound = form.sound.data
			session.user_id = g.user.id
			db.session.add(session)
			db.session.commit()
		if not id and form.validate_on_submit():
			print form.sound.data
			session = Session(
				title = form.title.data,
				description = form.description.data,
				sound = form.sound.data,
				user_id = g.user.id)
			db.session.add(session)
			db.session.commit()
		sessions = Session.query.all()
		files = os.listdir('app/static/uploaded')
		return render_template('cpanel_sessions.html', form = form, sessions = sessions, files = files, id = id)
	else:
		return render_template('access_err.html')

@app.route('/cpanel/news', methods = ['GET', 'POST'])
@app.route('/cpanel/news/<id>', methods = ['GET', 'POST', 'DELETE'])
@login_required
def cpanel_news(id = None):
	if g.user.admin:
		if request.method == 'DELETE' and id:
			db.session.delete(News.query.get(id))
			db.session.commit()
		form = AddNewsForm()
		if request.method == 'GET' and id:
			news = News.query.get(int(id))
			form.title.data = news.title
			form.description.data = news.description
		if request.method == 'POST' and id and form.validate_on_submit():
			news = News.query.get(int(id))
			news.title = form.title.data
			news.description = form.description.data
			news.time = datetime.now()
			news.user_id = g.user.id
			db.session.add(news)
			db.session.commit()
		if not id and form.validate_on_submit():
			news = News(
				title = form.title.data,
				description = form.description.data,
				time = datetime.now(),
				user_id = g.user.id)
			db.session.add(news)
			db.session.commit()
		allnews = News.query.all()
		return render_template('cpanel_news.html', form = form, allnews = allnews, id = id)
	else:
		return render_template('access_err.html')

@app.route('/cpanel/files', methods = ['GET', 'POST'])
@app.route('/cpanel/files/<name>', methods = ['GET', 'DELETE'])
@login_required
def files(name = None):
	if g.user.admin:
		if request.method == 'POST':
			file = request.files['file']
			filename = secure_filename(file.filename)
			file.save(os.path.join('app/static/uploaded',filename))
		if request.method == 'DELETE' and name:
			os.remove('app/static/uploaded/'+name)
		files = os.listdir('app/static/uploaded')
		return render_template('files.html', files = files)
	else:
		return render_template('access_err.html')

@app.route('/cpanel/users', methods = ['GET', 'POST'])
@login_required
def users():
	if g.user.admin:
		return render_template('cpanel_users.html')
	else:
		return render_template('access_err.html')
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

@app.route('/sessions/')
@app.route('/sessions/<id>')
def sessions(id = None):
	sessions = Session.query.all()
	sessions.reverse()
	if id:
		ss = Session.query.get(int(id))
		user = User.query.get(ss.user_id)
		return render_template('sessions.html', sessions = sessions, ss = ss, user = user)
	return render_template('sessions.html', sessions = sessions)

@app.route('/news/')
@app.route('/news/<id>',)
def news(id = None):
	allnews = News.query.all()
	allnews.reverse()
	if id:
		news = News.query.get(int(id))
		comments = Comments.query.filter_by(news_id = int(id))
		return render_template('news.html', allnews = allnews, news = news, comments = comments)
	return render_template('news.html', allnews = allnews)

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