import os, json, util
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func, insert, update

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)

# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data/data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)

# Class allows one to query the database
class Saves(db.Model):
    __tablename__= 'saves'
    name = db.Column(db.String(64), primary_key=True)
    json = db.Column(db.String(64))	

# Sends users to index page upon load
@app.route('/')
def index():
    return render_template("index.html")

# Sends users to about page upon load
@app.route('/about')
def about():
    return render_template('about.html')

# Sends users to game page upon load
@app.route('/game')
def game():
    return render_template('game.html')

# Receives JSON object with game state 
# DOES NOT MAKE CHANGES TO DB AT THIS POINT!
@app.route('/game/save/<userName>', methods=['POST'])
def save(userName):
    stateJSON = request.get_json()
    print(stateJSON)
    
    return "no saving yet"

# Returns JSON object associated with given username
# If name is not found, returns a string "failure"
@app.route('/game/load/<userName>', methods=['GET'])
def load(userName):
    if(Saves.query.filter(Saves.name == userName).count() > 0):
        return Saves.query.filter(Saves.name == userName).first().json
    else:
        return "failure"

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)