from location import location


class maze(location):
	def __init__(self, name, adjacent, closeness):
		super().__init__(
			name,
			adjacent,
			'As you ascend the stairs, you are met with a dimly-lit corridor. Each step you take sets forth a resounding echo. Stopping to listen carefully, you hear a faint voice in the distance.'
			)
		self.closeness = closeness

def getCloseness(self):
	return self.closeness


def getAdjacentString(self):
	adjString = "There are exits "

	for i in self.adjacent:
		adjString += i.upper() + ", "

	return adjString[:-1] + "."
