from app import app, db
from models import Member, Todos, TimerDetails
from forms import LoginForm, RegisterForm
from flask import render_template, flash, redirect, url_for, session, logging, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import logging

# initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return Member.query.get(int(user_id))

# Home page
@app.route('/')
def index():	
	return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		member = Member.query.filter_by(username=form.username.data).first()
		if member:
			if check_password_hash(member.password, form.password.data):
				login_user(member, remember=form.remember.data)
				session['logged_in'] = True
				return redirect(url_for('pomodoro'))
		else:
			pass #flash

	return render_template('login.html',form=form)


# user registration page
@app.route('/register', methods=["GET", "POST"])
def register():
	form = RegisterForm()

	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_member = Member(username=form.username.data, password=hashed_password, email=form.email.data)
		db.session.add(new_member)
		db.session.commit()
		return redirect(url_for('pomodoro'))
	else:
		return render_template('register.html',form=form)


# logout user
@app.route('/logout')
@login_required
def logout():
	session['logged_in'] = False
	logout_user()
	return redirect(url_for('index'))


# pomodoro-tracker page
@app.route('/pomodoro', methods=["GET", "POST"])
@login_required
def pomodoro():
	if request.method == 'POST':
		inputTimerTarget = request.form['pomodoroInterval']
		inputBreakTarget = request.form['breakInterval']
		# convert times to minutes:
		timerTarget = inputTimerTarget[3:]
		breakTarget = inputBreakTarget[3:]

		# save timer intervals for logged in user
		newTimerDetails = TimerDetails(member_username=current_user.username, pomodoro_interval=timerTarget, 
									   break_interval=breakTarget)
		db.session.add(newTimerDetails)
		db.session.commit()

		return render_template('pomodoro.html', timerTarget=timerTarget, breakTarget=breakTarget, 
												inputTimerTarget=inputTimerTarget, 
												inputBreakTarget=inputBreakTarget)
	else:
		timerDetails = TimerDetails.query.filter_by(member_username=current_user.username).first()
		if(timerDetails):
			inputTimerTarget = ('00:' + str(timerDetails.pomodoro_interval))
			inputBreakTarget = ('00:' + str(timerDetails.break_interval))
			return render_template('pomodoro.html', timerTarget=timerDetails.pomodoro_interval, 
													breakTarget=timerDetails.break_interval,
													inputTimerTarget=inputTimerTarget,
													inputBreakTarget=inputBreakTarget)
		else:
			return render_template('pomodoro.html', timerTarget=25, breakTarget=5, 
													inputTimerTarget=25, inputBreakTarget=5)


# todos scheduler
@app.route('/todos', methods=["GET", "POST"])
@login_required
def todos():
	todos = Todos.query.filter_by(member_username=current_user.username).all()
	return render_template('todos.html',todos=todos)


# feedback page
@app.route('/feedback')
def feedback():	
	pass