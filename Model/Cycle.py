class Cycle:
	def __init__(self, period, cadence, date_start, date_end, team_name, parent_period):
		self.period = period
		self.cadence = cadence
		self.date_start = date_start
		self.date_end = date_end
		self.team_name = team_name
		self.parent_period = parent_period
	
	@classmethod
	def fromlist(cls, list):
		return cls(list[0],list[1],list[2],list[3],list[4],list[5])
	
	def get_values_tuple(self):
		return (self.period, self.cadence, self.date_start, self.date_end, self.team_name, self.parent_period)

	def get_period(self):
		return self.period

	def get_cadence(self):
		return self.cadence

	def get_parent_period(self):
		return self.parent_period

	def get_date_start(self):
		return self.date_start

	def get_date_end(self):
		return self.date_end

	def get_team_name(self):
		return self.team_name

	def __str__(self):
 		return "period: " + self.period + " , " + "cadence: " + self.cadence + " , " + "parent_period: " + self.parent_period + " , " + "date_start: " + str(self.date_start) + " , " + "date_end: " + str(self.date_end) + " , " + "team_name: " + self.team_name
	
	def __repr__(self):
 		return "period: " + self.period + " , " + "cadence: " + self.cadence + " , " + "parent_period: " + self.parent_period + " , " + "date_start: " + str(self.date_start) + " , " + "date_end: " + str(self.date_end) + " , " + "team_name: " + self.team_name
