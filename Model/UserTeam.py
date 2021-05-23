class UserTeam:
	def __init__(self, user_email, team_name):
		self.user_email = user_email
		self.team_name = team_name
	
	@classmethod
	def fromlist(cls, list):
		return cls(list[0],list[1])
	
	def get_values_tuple(self):
		return (self.user_email, self.team_name)

	def get_user_email(self):
		return self.user_email

	def get_team_name(self):
		return self.team_name


	def __str__(self):
 		return "user_email: " + self.user_email + " , " + "team_name: " + self.team_name
	
	def __repr__(self):
 		return "user_email: " + self.user_email + " , " + "team_name: " + self.team_name
