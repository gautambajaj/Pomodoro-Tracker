from app import db

class Member(db.Model):
	name = db.Column(db.String(50), unique=False, nullable=False, primary_key=True)
