class interact:
	def __init__(self, text, answer=None, obj=None):
		# self.name = name
		self.text = text
		self.obj = obj
		self.answer = answer


	# def getName(self):
	# 	return self.name

	def getText(self):
		return self.text

	def getAnswer(self):
		return self.answer

	def getObj(self):
		return self.obj

	def getAnswerText(self):
		return "You receive " + self.obj + "."