import os, json
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

validCommands = ['go','get','use','talk','answer','inventory','leave']

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

# Sends users to game page 
@app.route('/game')
def game():
    return render_template('game.html')

# Receives user commands and returns updated state. 
@app.route('/game/command', methods=['POST'])
def gameCommand():
    stateJSON = request.get_json()

    # Command must match list of valid commands (duh!)
    command = stateJSON['lastCommand'].lower().strip().split(' ')
    invalid = True
    for x in validCommands:
        if command[0] == x:
            invalid = False

    if invalid:
        stateJSON['outputText'] = "Invalid command entered."
    else:
        stateJSON['outputText'] = "Valid command entered!"

    return json.dumps(stateJSON)

# Sends user to game page with a "loading" username set 
@app.route('/game/<userName>')
def loadGame(userName):
    if (Saves.query.filter(Saves.name == userName).count() > 0):
        return render_template('game.html', loadName=userName)
    else:
        return "Failed to load. Did you enter the correct username?"

# Receives JSON object with game state (needs a set username!)
# If name already exists, old one is deleted. Sad!
@app.route('/save/<userName>', methods=['POST'])
def save(userName):
    stateJSON = request.get_json()
    print(stateJSON)
    newSave = Saves(name=userName,json=json.dumps(stateJSON))
    if (Saves.query.filter(Saves.name == userName).count() > 0):
        print("old name")
        db.session.delete(Saves.query.filter(Saves.name == userName).first())
        db.session.add(newSave)
        db.session.commit()
    else:
        print("new name")
        db.session.add(newSave)
        db.session.commit()
    
    return "Success!"

# Returns JSON object associated with given username
# If name is not found, returns a string "failure"
@app.route('/load/<userName>', methods=['GET'])
def load(userName):
    print(userName)
    if(Saves.query.filter(Saves.name == userName).count() > 0):
        print(Saves.query.filter(Saves.name == userName).first().json)
        return Saves.query.filter(Saves.name == userName).first().json
    else:
        return "failed"

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
