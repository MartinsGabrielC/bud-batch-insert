class Objective:
	def __init__(self, title, cycle_period, team_name, owner_email):
		self.title = title
		self.cycle_period = cycle_period
		self.team_name = team_name
		self.owner_email = owner_email
	
	@classmethod
	def fromlist(cls, list):
		return cls(list[0],list[1],list[2],list[3])
	
	def get_values_tuple(self):
		return (self.title, self.cycle_period, self.team_name, self.owner_email)

	def get_title(self):
		return self.title

	def get_cycle_period(self):
		return self.cycle_period

	def get_team_name(self):
		return self.team_name

	def get_owner_email(self):
		return self.owner_email


	def __str__(self):
 		return "title: " + self.title + " , " + "cycle_period: " + self.cycle_period + " , " + "team_name: " + self.team_name + " , " + "owner_email: " + self.owner_email

	def __repr__(self):
 		return "title: " + self.title + " , " + "cycle_period: " + self.cycle_period + " , " + "team_name: " + self.team_name + " , " + "owner_email: " + self.owner_email