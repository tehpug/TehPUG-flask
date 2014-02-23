from app import db

class User(db.Model):
	"""Users info in database"""
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(50), index = True, unique = True)
	password = db.Column(db.String(64))
	email = db.Column(db.String(100), index = True, unique = True)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return True

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)

class Session(db.Model):
	"""sessions info in Database"""
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), index = True)
	description = db.Column(db.String(4000), index = True)
	sound = db.Column(db.String(200))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Session %r>' % (self.title)

class News(db.Model):
	"""News info in Database"""
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), index = True)
	description = db.Column(db.String(4000), index = True)
	time = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
			return '<News %r>' % (self.title)	