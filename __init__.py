import os, json
from karl import karl
from maze import maze
from world import world
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func, insert, update
from random import randrange


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

validCommands = ['go','get','use','talk','answer','leave']

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

    # TODO: CLEAN THIS SHIT UP. OH MY GOD!
    # Command must match list of valid commands (duh!)
    command = stateJSON['lastCommand'].lower().strip().split(' ', 1)
    invalid = True
    for x in validCommands:
        if command[0] == x:
            invalid = False

    if invalid:
        stateJSON['outputText'] = karlBadInput()
        return json.dumps(stateJSON)

    newWorld = world()

    if command[0] == "go":
        print("go")
        location = newWorld.navigate(command[1],stateJSON['currentLocation'])
        if location == False:
            stateJSON['outputText'] = karlBadInput()
        else:
            stateJSON['currentLocation'] = location
            stateJSON['outputText'] = newWorld.getmap()[location].getText()
            if type(newWorld.getmap()[location]) is maze:
                stateJSON['outputText'] += "×" + newWorld.getmap()[location].getAdjacentString()

    elif stateJSON['currentLocation'] == 'karl':
        gemcount = 0
        for i in stateJSON['inventory']:
            gemcount += stateJSON['inventory'][i]
        newKarl = karl()

        if command[0] == 'talk':
            question = newKarl.getQuestion(gemcount)
            stateJSON['outputText'] = newKarl.getText() + question 
        elif command[0] == 'answer':
            karlanswer = newKarl.isAnswerCorrect(gemcount,command[1])
            if karlanswer:
                stateJSON['currentLocation'] = 'goodend'
                stateJSON['outputText'] = '... You’ve done it” A purifying light emanates from Karl and explodes from him, growing brighter and larger. The light washes over you and the campus. The dreadful presence dissipates. The Swamps\' hold on the campus is released, and ECU is restored to its former beauty. It feels like a dream. Suddenly, you are jolted awake, staring at your computer screen in Austin 208. You must’ve fallen asleep while doing homework. Beside you, there is a candy bar with a note that simply says “Thank you”. You take a bite of it and get back to work. ×GOOD END.'
            else:
                stateJSON['currentLocation'] = 'badend'
                stateJSON['outputText'] = 'So close, yet so far. You displayed such hubris, but had nothing to show for it. This shameful display has sealed the fate of the campus. Good work. ×DEAD END.'

    elif command[0] == "answer":
        print("answer")
        answer = newWorld.answer(stateJSON['currentLocation'],command[1].lower())

        if answer == False:
            stateJSON['outputText'] = karlBadInput()
        else:
            stateJSON['inventory'][answer] = 1 
            stateJSON['outputText'] = "Great work! You receive " + answer + "."

    elif command[0] == "leave" and stateJSON['currentLocation'] == 'courtyard':
        print("leave")
        stateJSON['currentLocation'] = "leaveend"
        stateJSON['outputText'] = "Within minutes, the perils of the swamp are far behind you. But what about the others? Do you even care? ×NOPE END."
   
    elif len(command) < 2:
        stateJSON['outputText'] = karlBadInput()
    
    else:
        print("interact")
        interact = newWorld.talk(command[0],command[1].lower(),stateJSON['currentLocation'])
        if command[1].lower() == "candy bar" and command[0] == "get" and stateJSON['currentLocation'] == "austin208":
            stateJSON['currentLocation'] = "chocoend"
            stateJSON['outputText'] = "You snatch up the candy bar and DEVOUR it. Why would you do that? You keel over and die from the poisonous swamp chocolate. ×GASTRONOMIC END."
        elif interact == False:
            stateJSON['outputText'] = karlBadInput()
        elif command[1].lower() == "dr gopal":
            stateJSON['outputText'] = interact
            stateJSON['inventory']["Gopal's Proof"] = 1 
        else:
            stateJSON['outputText'] = interact
        

    return json.dumps(stateJSON)

# Makes karl shout at idiots
def karlBadInput():
    insultArr = ['Guessing is a disease!','This is nonsense!!!','You didn’t even try!!']
    return "A voice booms from across the swamp: " + insultArr[randrange(3)]


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
