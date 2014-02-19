from app import db

class User(db.Model):
	"""Users info in database"""
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(50), index = True, unique = True)
	email = db.Column(db.String(100), index = True, unique = True)

	def __repr__(self):
		return '<User %r>' % (self.username)
