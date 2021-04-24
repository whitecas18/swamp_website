from location import location
from maze import maze


class world:
	def __init__(self):
			self.map = self.createMap()


	def createMap(self):

		austin = location(
			"austin",
			{"north":"hoggard","west":"hills","south":"208", "east":"courtyard"},
			"ADD TEXT ADD TEXT")

		hills = location(
			"hills",
			{"east":"austin"},
			"Dr. Hills is in his office enjoying lunch. You hear birds chirping outside, feel the warmth of the sun permeating the blinds. Were it not for the derelict hallway behind you, the day would seem as fine as any other. It is almost as if his office is in another world… in the cloud?",
			{"talk":"dr hills"})

		hoggard = location("hoggard",
			{"south":"austin"},
			"The classroom is empty, barring one figure. Hoggard is standing next to the desk, eating cup noodles as his powerpoints slides rapidly flash by. He smiles when he sees you.",
			{"talk": "hoggard"})

		austin208 = location(
			"austin208",
			{"north: austin"},
			"The room is absolutely littered with chicken sandwich wrappers. There is also a pile of dubious looking CANDY BARS. Austin proper is to the NORTH",
			{"take": "candy bar"}
			)

		courtyard = location(
			"courtyard",
			{"west":"austin", "north":"libraryent"},
			"A strong breeze sends a chill down your spine. It is oppressively humid and there are no signs of life. Not even the chittering of the ECU squirrels."
			)

		libraryent = location(
			"libraryent",
			{"north":"library", "east":"scitech", "south":"courtyard"},
			"ADD TEXT ADD TEXT"
			)

		library = location(
			"library",
			{"east":"maze", "south":"libraryent"},
			"Dim green lighting greets you and a sour swamp-like smell fills your nostrils as you walk into the LIBRARY.  As you enter the foyer, you realize that the fluorescent lighting has been replaced by green torches that cover the walls, flickering ominously.  The sour smell seems to be emanating from a broken refrigerator from the obviously abandoned coffee shop to your left. Before you NORTH lies a staircase leading upwards.  An exit to the library is to the SOUTH."
			)

		scitech = location(
			"scitech",
			{"west":"libraryent", "north":"ding", "east":"wu", "south":"karl"},
			"The windows of the once great Sci Tech building are all shattered, and the swamp’s life is completely overtaking the building. The entrance way, however, is still reachable through the trees. There is knowledge here, you can feel it."
			)

		ding = location(
			"ding",
			{"south":"scitech"},
			"Dr. Ding is in her office, frantically writing relational algebra queries while muttering to herself. The walls, floor, and windows are covered with them, and she is writing more on the ceiling. She looks down at you as you enter but doesn’t leave the ceiling.",
			{"talk":"dr ding"}
			)

		wu = location(
			"wu",
			{"west":"scitech"},
			"You hear the sound of a thousand GPUs whirring away, analyzing dataset after dataset of dubious origin. Curiously, not a single one of them is in sight. The residual heat, however, is readily felt. Dr. Wu is at his battlestation, typing away.",
			{"talk":"dr wu"}
			)

		karl = location(
			"karl",
			{"north":"scitech"}
			"You enter the SciTech basement. There is not a single window; piles of computers extend as far as the eye can see. Wires hang from the ceiling, leading to nowhere in particular. You see Karl working on a computer with a large smiley face stamped on the side.",
			{"talk":"karl"}
			)

		mazeentry = location(
			"mazestart",
			{"west":"library"},
			"As you ascend the stairs, you are met with a dimly-lit corridor. Each step you take sets forth a resounding echo. Stopping to listen carefully, you hear a faint voice in the distance... WEST leads you back to the LIBRARY. EAST leads you deeper..."
			)

		maze1 = maze(
			"maze1"
			{"east":"mazeentry", "west"}
			)

		ronnie = location()