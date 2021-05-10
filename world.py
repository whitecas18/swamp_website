from location import location
from maze import maze
from interact import interact
from karl import karl
from random import randrange


class world:
    def __init__(self):
        self.map = self.createMap()
        self.interactions = {
            "dr hills": interact(
                "Hey, go ahead and shut that door behind you. Crazy day isn’t? Good thing I backed up yesterday in the Cloud or my office would be a disaster. Karl has gone a little off the rails with this Swamp thing, but I’m sure if you just go talk to him, he’ll undo it. Before you go, quick question.× Which of the following is not defined as an important characteristic of virtualization?× ( Fidelity, Performance, Low Power Consumption, Isolation/Safety)",
                "low power consumption",
                "Hills’ API",
            ),

            "dr ding": interact(
                "Have you ever considered existence itself…. Is a database? The grounds may be empty…. but the tuples…. the tuples are filled. Filled with every soul that has been…. And ever will be. My knowledge is not free…. You must answer me this...× Which relational algebra operation does the SQL select clause map to?× (Select/Project/Cartesian Product/Union) ",
                "project",
                "Ding’s Database"
            ),

            "dr wu": interact(
                "It’s no use. No matter how many GPUs I have none of this data makes any sense. The Swamp’s expansion cannot be stopped. Your only hope is to go to the source. You’ll need my knowledge if you hope to survive.×Which portion of this URL identifies the process on the host machine? https://www.cs.ecu.edu/?word=hello ×(https/cs/?word/none)",
                "none",
                "Wu’s Library"
            ),

            "hoggard": interact(
                "Just because the campus has been overwhelmed by a swamp doesn’t excuse you being late to my class. Luckily, you’re just in time for a pop quiz. Closed notes of course.×Which of the following is an email access protocol?×(MIME/SMTP/IMAP/RFC2822)",
                "imap",
                "Hoggard’s Syntax"
            ),

            "computer": interact(
                "SMITHR@CSHRINE ~> Greetings. I had my doubts you’d find this place. I thought about leaving instructions in Austin 208 but that’d wouldn’t be much of a test, would it?  Probably should have given you a heads up about the candy bars though. Your reward for finding this location is a question. Don’t worry, this is an easy one×What is the maximum number of edges in a directed graph with n nodes? (assuming no edges to themself)×(n*(n-1)), (n/(n-1)), (n+(n-1)), (n*(n+1))"
                "n*(n-1)",
                "Ronnie’s Insight"
            ),

            "dr gopal": interact(
                "Put it to garbage Put it to garbage Put it to ggarbage Putitto garbage Put it to gar age Put it to garbage! Put it to garbage Put itto garbage Put it to gARBage Put it to garbage PPut it to garbgae Put it to g a r b a g e Put it to gArBaGe PutItToGarbage!!! ×You received Gopal's Proof",
                None,
                "Gopal's Proof"
            ),

            "candy bar": interact(
                "HUZZAH! The candy bar is yours!",
                None,
                "Chocolate Bar"
            ),
            "karl": karl()
        }

    def createMap(self):

        chocoend = location(
            "chocoend",
            {},
            "Why would you do that? The five second rule is one thing… but the five-thousand year rule..? ×GASTRONOMIC END.",
            {})

        leaveend = location(
            "leaveend",
            {},
            "Within minutes, the perils of the swamp are far behind you. But what about the others? Do you even care? ×LEAVE END.",
            {})

        badend = location(
            "badend",
            {},
            "So close, yet so far. You displayed such hubris, but had nothing to show for it. This shameful display has sealed the fate of the campus. Good work. ×DEAD END.",
            {})

        goodend = location(
            "goodend",
            {},
            "... You’ve done it” A purify light emanates from Karl and explodes from him, growing brighter and larger. The light washes over you and campus. The dreadful presence dissipates from the campus. The Swamps hold on the campus is released, and ECU is restored to its former beauty. It feels like a dream. Suddenly, you are jolted awake, staring at your computer screen in Austin 208. You must’ve fallen asleep while doing homework. Beside you, there is a candy bar with a note that simply says “Thank you”. You take a bite of it and get back to work. GOOD END.",
            {})

        austin = location(
            "austin",
            {"north": "hoggard", "west": "hills",
                "south": "austin208", "east": "courtyard"},
            "The ground of the hallway feels as if it’d pull you in if you stood there too long. It may be your imagination, but it seems as if the hallway itself is rotating. The other classrooms are almost inaccessible. The large, crawling vines make traversal through the hall a dangerous task.× To the NORTH lies and an office labeled “HOGGARD”. To the WEST lies an office labeled “HILLS”. To the SOUTH lies Austin 208. To the EAST lies the exit to campus proper.",
            {})

        hills = location(
            "hills",
            {"east": "austin"},
            "DR HILLS is in his office enjoying lunch. You hear birds chirping outside, feel the warmth of the sun permeating the blinds. Were it not for the derelict hallway behind you, the day would seem as fine as any other. It is almost as if his office is in another world… × To the EAST is the office exit, back into chaos of the swamp",
            {"talk": "dr hills"})

        hoggard = location("hoggard",
                           {"south": "austin"},
                           "The classroom is empty, barring one figure. HOGGARD is standing next to the desk, eating cup noodles as his powerpoints slides rapidly flash by. He smiles when he sees you.× To the SOUTH is the office exit",
                           {"talk": "hoggard"})

        austin208 = location(
            "austin208",
            {"north": "austin"},
            "The room is absolutely littered with chicken sandwich wrappers. There is also a dubious looking CANDY BAR. ×Austin proper is to the NORTH",
            {"get": "candy bar"}
        )

        courtyard = location(
            "courtyard",
            {"west": "austin", "north": "libraryent"},
            "A strong breeze sends a chill down your spine. It is oppressively humid and there are no signs of life. Not even the chittering of the ECU squirrels. Glancing at the entrance of the campus, you feel an urgent need to escape. × To the NORTH lies the pathway to the LIBRARY. To the WEST is the AUSTIN building. The silence is deafening.",
            {})

        libraryent = location(
            "libraryent",
            {"north": "library", "east": "scitech", "south": "courtyard"},
            "Despite the chaotic state the campus is in, The Library remains intact. The putrid smell that coats the campus is even stronger here. Green light glows through the glass of the double doors. ×To the NORTH lies the LIBRARY doors. To the EAST lies the SCI-TECH building. To the SOUTH lies the COURTYARD",
            {})

        library = location(
            "library",
            {"east": "entrymaze", "south": "libraryent"},
            "Dim green lighting greets you and a sour, swamp-like smell fills your nostrils as you walk into the LIBRARY.  As you enter the foyer, you realize that the fluorescent lighting has been replaced by green torches that cover the walls, flickering ominously.  The sour smell seems to be emanating from a broken refrigerator from the obviously abandoned coffee shop to your left. × To the EAST lies a staircase leading upwards.  An exit to the LIBRARY is to the SOUTH.",
            {})

        scitech = location(
            "scitech",
            {"west": "libraryent", "north": "ding", "east": "wu", "south": "karl"},
            "The windows of the once great Sci Tech building are all shattered, and the swamp’s life is completely overtaking the building. The entrance way, however, is still reachable through the trees. There is knowledge here, you can feel it. × To the EAST lies an office labeled ‘WU”.  To the NORTH lies an office labeled “DING”. To the WEST is the LIBRARY. To the SOUTH is a dark portal, ready to suck you in to face Karl in your final battle. Be sure and explore to make sure you're ready.",
            {})

        ding = location(
            "ding",
            {"south": "scitech"},
            "DR DING is in her office, frantically writing relational algebra queries while muttering to herself. The walls, floor, and windows are covered with them, and she is writing more on the ceiling. She looks down at you as you enter but doesn’t leave the ceiling. × To the SOUTH is the office exit",
            {"talk": "dr ding"}
        )

        wu = location(
            "wu",
            {"west": "scitech"},
            "You hear the sound of a thousand GPUs whirring away, analyzing dataset after dataset of dubious origin. Curiously, not a single one of them is in sight. The residual heat, however, is readily felt. DR WU is at his battlestation, typing frantically. × To the WEST is the office exit",
            {"talk": "dr wu"}
        )

        karl = location(
            "karl",
            {"north": "scitech"},
            "You enter the SciTech basement. There is not a single window; piles of computers extend as far as the eye can see. Wires hang from the ceiling, leading to nowhere in particular. You see KARL working on a computer with a large smiley face stamped on the side. No use trying to escape now...",
            {"talk": "karl"}
        )

        entrymaze = location(
            "mazestart",
            {"west": "library", "east": "maze1"},
            "As you ascend the stairs, you are met with a dimly-lit corridor. Each step you take sets forth a resounding echo. Stopping to listen carefully, you hear a faint voice in the distance... × WEST leads you back to the LIBRARY. EAST leads you deeper...",
            {})

        maze1 = maze(
            "maze1",
            {"west": "entrymaze", "east": "maze2"},
            1
        )

        maze2 = maze(
            "maze2",
            {"west": "maze1", "north": "maze3"},
            1
        )

        maze3 = maze(
            "maze3",
            {"south": "maze2", "east": "maze4", "west": "maze5", "north": "maze6"},
            2
        )

        maze4 = maze(
            "maze4",
            {"east": "ronnie", "west": "maze3"},
            2
        )

        maze5 = maze(
            "maze5",
            {"east": "maze3", "west": "maze7", "north": "maze8"},
            2
        )

        maze6 = maze(
            "maze6",
            {"south": "maze3", "east": "maze9"},
            3
        )

        maze7 = maze(
            "maze7",
            {"east": "maze5", "north": "maze10"},
            1
        )

        maze8 = maze(
            "maze8",
            {"south": "maze7", "west": "maze10"},
            3
        )

        maze9 = maze(
            "maze9",
            {"north": "maze11", "west": "maze6"},
            3
        )

        maze10 = maze(
            "maze10",
            {"east": "maze8", "south": "maze7"},
            2
        )

        maze11 = maze(
            "maze11",
            {"south": "maze9", "west": "maze12"},
            4
        )

        maze12 = maze(
            "maze12",
            {"east": "maze11", "north": "gopal"},
            5
        )

        ronnie = location(
            "ronnie",
            {"west": "maze4"},
            "Another dead end… or is it? While there is no room or door in sight, there is an old COMPUTER sitting on a table in front of you. It is surrounded by candles and a single prompt is displayed on the screen. SMITHR@CSHRINE ~> | To the WEST is the exit back into the maze",
            {"use": "computer"}
        )

        gopal = location(
            "gopal",
            {"south": "library"},
            "You finally reach the source of the sound. DR GOPAL sits alone in a library study room. In front of him is a 3 monitors setup, none of which are turned on. DR GOPAL is holding a microphone chanting the same phrase repeatedly into it. He doesn’t even notice you, too focused on his “recording”. | To the SOUTH is the exit back into the maze",
            {"talk": "dr gopal"}
        )

        return {"chocoend": chocoend, "leaveend": leaveend, "gooend": goodend, "badend": badend, "austin": austin, "hills": hills, "hoggard": hoggard, "austin208": austin208, "courtyard": courtyard, "libraryent": libraryent, "library": library, "scitech": scitech, "ding": ding, "wu": wu, "karl": karl, "entrymaze": entrymaze, "maze1": maze1, "maze2": maze2, "maze3": maze3, "maze4": maze4, "maze5": maze5, "maze6": maze6, "maze7": maze7, "maze8": maze8, "maze9": maze9, "maze10": maze10, "maze11": maze11, "maze12": maze12, "ronnie": ronnie, "gopal": gopal}

    def getmap(self):
        return self.map

    def navigate(self, direction, currentLoc):
        if direction in self.map[currentLoc].getAdjacent():
            return self.map[currentLoc].getAdjacent()[direction]
        else:
            return False

    # If valid direction is entered, player is moved to desired location
    def go(self, stateDict, command):
        location = self.navigate(command[1], stateDict['currentLocation'])
        if location == False:
            stateDict['outputText'] = "Nothing that way..."
        else:
            stateDict['currentLocation'] = location
            stateDict['outputText'] = self.getmap()[location].getText()
            if type(self.getmap()[location]) is maze:
                stateDict['outputText'] += "×" + \
                    self.getmap()[location].getAdjacentString()

        return stateDict

    # Players may only "leave" when in the courtyard location. Special ending.
    def leave(self, stateDict):
        if stateDict['currentLocation'] == 'courtyard':
            stateDict['currentLocation'] = "leaveend"
            stateDict['outputText'] = "Within minutes, the perils of the swamp are far behind you. But what about the others? Do you even care? ×NOPE END."
        else:
            stateDict['outputText'] = "There is no apparent means of escape here"

        return stateDict

    # Special handler for all dealings with Karl. Because he's special.
    def karl(self, stateDict, command):
        gemcount = 0
        for i in stateDict['inventory']:
            gemcount += stateDict['inventory'][i]
        newKarl = karl()

        # Retreives the correct question forcurrent gem count
        if command[0] == 'talk':
            question = newKarl.getQuestion(gemcount)
            stateDict['outputText'] = newKarl.getText() + question

        # Determines whether given answer is correct
        elif command[0] == 'answer':
            karlanswer = newKarl.isAnswerCorrect(gemcount, command[1])
            if karlanswer:
                stateDict['currentLocation'] = 'goodend'
                stateDict['outputText'] = '... You’ve done it” A purifying light emanates from Karl and explodes from him, growing brighter and larger. The light washes over you and the campus. The dreadful presence dissipates. The Swamps\' hold on the campus is released, and ECU is restored to its former beauty. It feels like a dream. Suddenly, you are jolted awake, staring at your computer screen in Austin 208. You must’ve fallen asleep while doing homework. Beside you, there is a candy bar with a note that simply says “Thank you”. You take a bite of it and get back to work. ×GOOD END.'
            else:
                stateDict['currentLocation'] = 'badend'
                stateDict['outputText'] = 'So close, yet so far. You displayed such hubris, but had nothing to show for it. This shameful display has sealed the fate of the campus. Good work. ×DEAD END.'

        return stateDict

    # Determines whether given answer is correct for all prof aside from Karl
    def answer(self, stateDict, answer):
        currentLoc = stateDict['currentLocation']
        if currentLoc == "ronnie" and answer == "n*(n-1)":
            stateDict['inventory']["Ronnie's Insight"] = 1
            stateDict['outputText'] = "Great work! You receive Ronnie's Insight"
        elif currentLoc == "wu" and answer == "none":
            stateDict['inventory']["Wu's Library"] = 1
            stateDict['outputText'] = "Great work! You receive Wu's Library"
        elif currentLoc == "hills" and answer == "low power consumption":
            stateDict['inventory']["Hills' API"] = 1
            stateDict['outputText'] = "Great work! You receive Hills' API"
        elif currentLoc == "hoggard" and answer == "imap":
            stateDict['inventory']["Hoggard's Syntax"] = 1
            stateDict['outputText'] = "Great work! You receive Hoggard's Syntax"
        elif currentLoc == "ding" and answer == "project":
            stateDict['inventory']["Ding's Database"] = 1
            stateDict['outputText'] = "Great work! You receive Ding's Database"
        else:
            stateDict['outputText'] = self.karlBadInput() + " (incorrect answer)"

        return stateDict

    # General "interact" function. Handles get, talk, and use verbs!
    def interact(self, stateDict, command):
        currentLoc = stateDict['currentLocation']
        loc = self.map[currentLoc]
        verb = command[0]
        obj = command[1]

        # Special chocolate ending. Only instance of "get" command
        if command[1].lower() == "candy bar" and command[0] == "get" and stateDict['currentLocation'] == "austin208":
            stateDict['currentLocation'] = "chocoend"
            stateDict['outputText'] = "You snatch up the candy bar and DEVOUR it. Why would you do that? You keel over and die from the poisonous swamp chocolate. ×GASTRONOMIC END."
        # Talking to gopal works as if answering a question, for the maze itself is a puzzle.
        elif command[1].lower() == "dr gopal":
            stateDict['outputText'] = self.interactions[obj].getText()
            stateDict['inventory']["Gopal's Proof"] = 1
        # All other interaction cases have been dealt with in a more... elegant manner
        elif verb in loc.getInteract():
            if loc.getInteract()[verb] == obj:
                if currentLoc == "ronnie" and verb.lower() == "use" or verb.lower() == "talk":
                    stateDict['outputText'] = self.interactions[obj].getText()
        else: stateDict['outputText'] = self.karlBadInput() + " (invalid interaction)"

        return stateDict

    # Makes karl shout at idiots
    def karlBadInput(self):
        insultArr = ['Guessing is a disease!',
                     'This is nonsense!!!', 'You didn’t even try!!']
        return "A voice booms from across the swamp: " + insultArr[randrange(3)]
