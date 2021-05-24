class User:
	def __init__(self, first_name, last_name, nickname, linked_in_profile_address, role, email, part, picture, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.nickname = nickname
		self.linked_in_profile_address = linked_in_profile_address
		self.role = role
		self.email = email
		self.part = part
		self.picture = picture
		self.gender = gender
	
	@classmethod
	def fromlist(cls, list):
		return cls(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8])
	
	def get_values_tuple(self):
		return (self.first_name, self.last_name, self.nickname, self.linked_in_profile_address, self.role, self.email, self.picture, self.gender, self.authz_sub)

	def set_id(self, id):
		self.id = id

	def set_authz_sub(self, id):
		self.authz_sub = id
	
	def get_id(self):
		return self.id

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_nickname(self):
		return self.nickname

	def get_linked_in_profile_address(self):
		return self.linked_in_profile_address

	def get_about(self):
		return self.about

	def get_email(self):
		return self.email

	def get_role(self):
		return self.role

	def get_picture(self):
		return self.picture

	def get_gender(self):
		return self.gender
	
	def get_authz_sub(self):
		return self.authz_sub

	def __str__(self):
 		return "first_name: " + self.first_name + " , " + "last_name: " + self.last_name + " , " + "nickname: " + self.nickname + " , " + "linked_in_profile_address: " + self.linked_in_profile_address + " , " + "role: " + self.role + " , " + "email: " + self.email + " , " + "part: " + self.part + " , " + "picture: " + self.picture + " , " + "gender: " + self.gender
	
	def __repr__(self):
		return "first_name: " + self.first_name + " , " + "last_name: " + self.last_name + " , " + "nickname: " + self.nickname + " , " + "linked_in_profile_address: " + self.linked_in_profile_address + " , " + "role: " + self.role + " , " + "email: " + self.email + " , " + "part: " + self.part + " , " + "picture: " + self.picture + " , " + "gender: " + self.gender