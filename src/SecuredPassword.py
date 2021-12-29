import json

class SecuredPassword():
	alias=''
	password=''
	def __init__(self, alias,password):
			self.alias = alias
			self.password = password
	def toJson(self):
		return json.dumps(self, default=lambda o: o.__dict__)
