from app import db
from hashlib import sha256

class User(db.Model):
	"""Users info in database"""
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(50), index = True, unique = True)
	password = db.Column(db.String(64))
	email = db.Column(db.String(100), index = True, unique = True)

	def hash_pass(self, password):
		self.h_password = sha256(password).hexdigest()

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
