from app import db
from flask_login import UserMixin
from datetime import datetime

class Member(UserMixin, db.Model):
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(50))


class Todos(db.Model):
	id = db.Column(db.Integer(), primary_key=True, unique=True, autoincrement=True)
	member_username = db.Column(db.String(50))
	category = db.Column(db.String(50), nullable=True)
	description = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Boolean(), default=False)
	create_date = db.Column(db.DateTime(), default=datetime.now())


class TimerDetails(db.Model):
	id = db.Column(db.Integer(), primary_key=True, unique=True, autoincrement=True)
	member_username = db.Column(db.String(50))
	pomodoro_interval = db.Column(db.Integer())
	break_interval = db.Column(db.Integer())
