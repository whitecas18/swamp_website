import os, json, util
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)


# Sends users to index page upon load
@app.route('/')
def index():
    return render_template('index.html')

# Sends users to about page upon load
@app.route('/about')
def about():
    return render_template('about.html')

# Sends users to game page upon load
@app.route('/game')
def game():
    return render_template('game.html')


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)