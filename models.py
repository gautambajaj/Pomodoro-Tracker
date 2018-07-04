from app import db

class Member(db.Model):
	name = db.Column()
	username = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
	password = db.Column(db.String(150), nullable=False)
	confirm_password = db.Column(db.String(150), nullable=False)


class Todos(db.Model):
	id = db.Column(db.Integer(), primary_key=True, unique=True, autoincrement=True)
	member_username = db.Column(db.String(50), db.ForeignKey('Member.username'))
	category = db.Column(db.String(50), nullable=True)
	description = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Boolean(), default=False)
	create_date = db.Column(db.TIMESTAMP())
