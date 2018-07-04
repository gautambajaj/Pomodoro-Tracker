from app import app, db
from models import Member
from forms import LoginForm
from flask import render_template

@app.route('/')
def index():
	# newMember = Member(name="manas")
	# db.session.add(newMember)
	# db.session.commit()

	firstMember = Member.query.first()
	return '<h1>The first member is: ' + firstMember.name + '</h1>'


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('home.html',form=form)