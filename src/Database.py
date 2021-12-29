from SecuredPassword import SecuredPassword


import json
class Database():
	username=''
	masterPW=''
	securedPasswords=[]

	def __init__(self, username,masterPW):
		self.username = username
		self.masterPW = masterPW
	def toJson(self):
			return json.dumps(self, default=lambda o: o.__dict__)