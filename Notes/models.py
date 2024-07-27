from datetime import datetime
from flask import current_app
from itsdangerous import URLSafeTimedSerializer as Serializer
from Notes import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	post = db.relationship('Post', backref='author', lazy=True)

	def get_reset_token(self, expires=1800):
		s = Serializer(current_app.config['SECRET_KEY'], expires)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])

		try:
			user_id = s.loads(token)['user_id'] 
		except Exception as e:
			return None

		return User.query.get(user_id)


	def __repr__(self):
		return f"User('{self.id},{self.username}, '{self.email}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	path = db.Column(db.String(300), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	branch = db.Column(db.String(50), nullable=False)
	category = db.Column(db.String(50), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.id}, {self.title}, '{self.date_posted}')"
