from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('db_config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from views import *	 

if __name__ == '__main__':
	app.run(debug=True)