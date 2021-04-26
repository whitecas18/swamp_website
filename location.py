

#self.name is location name(string)
#self.adjacent is a dictionary of all adjacent locations keyed by compass
#self.text is the string that displays when you are in an area
#self.interact is a dictionary of all interactables in the location keyed to the verb to use the interactable
class location:
	def __init__(self, name, adjacent, text, interact = None):
		self.name = name
		self.adjacent = adjacent
		self.text = text
		self.interact = interact


	def getName(self):
		return self.name

	def getAdjacent(self):
		return self.adjacent

	def getText(self):
		return self.text

	def getInteract(self):
		return self.interact

	def getAdjacentString(self):
		adjString = " There are exits "

		for i in self.adjacent:
			adjString += i.upper() + ", "

		return adjString[:-2] + "."
