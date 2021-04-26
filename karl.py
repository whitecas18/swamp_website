class karl:
	def __init__(self):
		self.questions = [
			"Does P=NP?(Y/N)",
			"Write a regular expression that consists of all strings over alphabet {a, b} that have aabb as a contiguous substring(U is union)(No spaces).",
			"Given an arbitrary non-deterministic finite automaton (NFA) with N states, the maximum number of states in an equivalent minimized DFA is at least×(N^2, 2^N, 2N, N!)",
			"Suppose R is a binary relation on the set of real numbers where xRy iff 3x + 3y = 2. Which of the following is correct?× (R is symmetric, R is neither reflexive symmetric nor transitive, R is reflexive, R is transitive)",
			"What Key combination is used to exit emacs?×( C-x C-c, C-c x-c, C-C C-c, X-c C-c)",
			"If S is {2, 4, 6} × {8, 10, 12, 14}, what is |S|?×(7, 16, 8, 12)",
			"If p and q are both false then p -> q is false.× (True, False)"
			]

		self.answers = [
			"Ph'nglui mglw'nafh Karl R'lyeh wgah'nagl fhtagn",
			"(aUb)∗aabb(aUb)∗",
			"2^N",
			"R is symmetric",
			"C-x C-c",
			"12",
			"False",
			]

		self.text = "I’ve been waiting for you. The Swamp has been waiting for you. I desire a challenge. The Swamp desires a tribute.  I have a question for you. The Swamp has only the abyss for you. Your fate is sealed by your answer× (It looks like you only get one shot at this!) "

	def getText(self):
		return self.text

	def getQuestion(self, gemNum):
		return self.questions[gemNum]

	def isAnswerCorrect(self, gemNum, answer):
		if answer == self.answers[gemNum].lower():
			return True
		return False