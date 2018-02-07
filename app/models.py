from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from . import db
from datetime import datetime
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


class Pitch(db.Model):
	__tablename__='pitches'
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String)
	body=db.Column(db.String)
	time=db.Column(db.DateTime,default=datetime.utcnow)
	author=db.Column(db.String)	
	category=db.Column(db.String)
	posted = db.Column(db.DateTime, default=datetime.utcnow)

def save_pitches(self):
	db.session.add(self)
	db.session.commit()

@classmethod
def get_pitches(cls):
	pitches=Pitch.query.all()
	return pitches
@classmethod
def get_categories(cls,category):
	pitch_category=Pitch.query.filter_by(category = category)
	return pitch_category
all_pitches=[]

def __init__(self,title,body,author,category):
	self.title=title
	self.body=body
	self.author=author
	self.category=category



class User(UserMixin,db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255))
	email=db.Column(db.String(255),unique=True,index=True)
	bio=db.Column(db.String(255))
	profile_pic_path=db.Column(db.String(255))
	pass_secure = db.Column(db.String(255))

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








