class Team:
	def __init__(self, name, description, parent_name, gender, owner_email):
		self.name = name
		self.description = description
		self.parent_name = parent_name
		self.gender = gender
		self.owner_email = owner_email
	
	@classmethod
	def fromlist(cls, list):
		return cls(list[0],list[1],list[2],list[3],list[4])
	
	def get_values_tuple(self):
		return (self.name, self.description, self.parent_name, self.gender, self.owner_email)

	def get_name(self):
		return self.name

	def get_description(self):
		return self.description

	def get_parent_name(self):
		return self.parent_name

	def get_gender(self):
		return self.gender

	def get_owner_email(self):
		return self.owner_email

	def __str__(self):
 		return "name: " + self.name + " , " + "description: " + self.description + " , " + "parent: " + self.parent_name + " , " + "gender: " + self.gender + " , " + "owner: " + self.owner_email
	
	def __repr__(self):
 		return "name: " + self.name + " , " + "description: " + self.description + " , " + "parent: " + self.parent_name + " , " + "gender: " + self.gender + " , " + "owner: " + self.owner_email
