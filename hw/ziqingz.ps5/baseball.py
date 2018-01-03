class BaseballPlayer:
	def __init__(self, first_name, last_name, team, position, hit = 0, at_bats = 0):
		self.first_name = first_name
		self.last_name = last_name
		self.team = team
		self.position = position
		self.hit = hit
		self.at_bats = at_bats

	def record_atbat(self, whether_hit):
		if whether_hit:
			self.hit += 1
		self.at_bats += 1

	def batting_average(self):
		try:
			return self.hit / self.at_bats
		except ZeroDivisionError:
			return None

	def __lt__(self, other):
		if self.batting_average() < other.batting_average():
			return True
		elif self.batting_average() == other.batting_average():
			if self.last_name > other.last_name:
				return True
			elif self.last_name == other.last_name:
				if self.first_name > other.first_name:
					return True
		return False

	def __le__(self, other):
		return self.__lt__(other) or self.__eq__(other)

	def __gt__(self, other):
		if self.batting_average() > other.batting_average():
			return True
		elif self.batting_average() == other.batting_average():
			if self.last_name < other.last_name:
				return True
			elif self.last_name == other.last_name:
				if self.first_name < other.first_name:
					return True
		return False

	def __ge__(self, other):
		return self.__gt__(other) or self.__eq__(other)


	def __eq__(self, other):
		return self.batting_average() == other.batting_average() and self.last_name == other.last_name and self.first_name == other.first_name

	def __ne__(self, other):
		return self.__lt__(other) or self.__gt__(other)
