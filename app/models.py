from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from . import db
from datetime import datetime
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))




class User(UserMixin,db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255))
	email=db.Column(db.String(255),unique=True,index=True)
	bio=db.Column(db.String(255))
	profile_pic_path=db.Column(db.String(255))
	pass_secure = db.Column(db.String(255))
	pitchs=db.relationship('Pitch',backref='user',lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('You cannot read the attribute')

	@password.setter
	def password(self,password):
		self.pass_secure=generate_password_hash(password)

	def verify_password(self,password):
		return check_password_hash(self.pass_secure,password)




	def __repr__(self):
		return f'User {self.username}'


class Pitch(db.Model):
	__tablename__='pitches'
	id=db.Column(db.Integer,primary_key=True)
	head=db.Column(db.String(255))
	body=db.Column(db.String(255))
	time=db.Column(db.DateTime,default=datetime.utcnow)
	user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
	category_id=db.Column(db.Integer,db.ForeignKey('categories.id'))	

	def __repr__(self):
		return f'User{self.review}'

class Category(db.Model):
	__tablename__='categories'
	id=db.Column(db.Integer,primary_key=True)
	review=db.Column(db.String(255))
	pitchcat=db.relationship('Pitch',backref='category',lazy='dynamic')


