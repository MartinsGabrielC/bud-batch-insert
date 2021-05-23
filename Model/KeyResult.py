class KeyResult:
	def __init__(self, title, description, type, format, goal, initial_value, cycle_period, team_name, objective_title, owner_email):
		self.title = title
		self.description = description
		self.type = type
		self.format = format
		self.goal = goal
		self.initial_value = initial_value
		self.cycle_period = cycle_period
		self.objective_title = objective_title
		self.team_name = team_name
		self.owner_email = owner_email

	@classmethod
	def fromlist(cls, list):
		return cls(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9])
	
	def get_values_tuple(self):
		return (self.title, self.description, self.type, self.format, self.goal, self.initial_value, self.cycle_period, self.team_name, self.objective_title, self.owner_email)

	def get_title(self):
		return self.title

	def get_description(self):
		return self.description

	def get_type(self):
		return self.type

	def get_format(self):
		return self.format

	def get_goal(self):
		return self.goal

	def get_initial_value(self):
		return self.initial_value

	def get_cycle_period(self):
		return self.cycle_period

	def get_objective_title(self):
		return self.objective_title

	def get_team_name(self):
		return self.team_name

	def get_owner_email(self):
		return self.owner_email


	def __str__(self):
 		return "title: " + self.title + " , " + "description: " + self.description + " , " + "type: " + self.type + " , " + "format: " + self.format + " , " + "goal: " + str(self.goal) + " , " + "initial_value: " + str(self.initial_value) + " , " + "cycle_period: " + self.cycle_period + " , " + "objective_title: " + self.objective_title + " , " + "team_name: " + self.team_name + " , " + "owner_email: " + self.owner_email

	def __repr__(self):
 		return "title: " + self.title + " , " + "description: " + self.description + " , " + "type: " + self.type + " , " + "format: " + self.format + " , " + "goal: " + str(self.goal) + " , " + "initial_value: " + str(self.initial_value) + " , " + "cycle_period: " + self.cycle_period + " , " + "objective_title: " + self.objective_title + " , " + "team_name: " + self.team_name + " , " + "owner_email: " + self.owner_email