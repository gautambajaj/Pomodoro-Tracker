from app import app, db
from models import Member
from forms import LoginForm
from flask import render_template, flash, redirect, url_for, session, logging, request


# Home page
@app.route('/')
def index():
	# newMember = Member(name="manas")
	# db.session.add(newMember)
	# db.session.commit()

	# firstMember = Member.query.first()
	return render_template('home.html')


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',form=form)


# user registration page
@app.route('/register')
def register():
	pass

# pomodoro-tracker page
@app.route('/pomodoro')
def pomodoro():
	return render_template('pomodoro.html')

# feedback page
@app.route('/feedback')
def feedback():	
	pass