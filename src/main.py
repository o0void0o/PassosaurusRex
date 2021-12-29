import json
import os
from SecuredPassword  import SecuredPassword
from Database import Database
from types import SimpleNamespace

DB_NAME='database.json'
database= {}
username=''
db={}

def loadDatabase():
	# convert into JSON:
	try:

		with open("database.json", "r") as read_file:
			print("Converting JSON encoded data into Python dictionary")
			x = json.load(read_file)
			
	
	
		return x
	except Exception as e: 
		print(e)
		print("SAD FACE")
		return {}



def init():
	print("init method")
	if doesDBExists():
		print("DB does exist")
		if doesUserExists():
			print("User does exist")
			if validateMasterPassword(promptForMasterPassword()):
				print("elooos")	
			else:
				print("nope")		
		else:
			print("User does not exist")
			registerAnewUser()


	else:
		print("DB does not exist")
		registerAnewUser()

def registerAnewUser():
	db["username"]=promptForNewUsername()
	db["password"]=promptForNewMasterPassword()
	save_data(db) # saving the json file




def doesDBExists():
	return os.path.exists(DB_NAME)

	 

def doesUserExists():
	global database
	database = loadDatabase()
	print("HI")
	print(database['username'])
	# database['securedPasswords']=[]
	# database.username=db.username
	# database.masterPW=db.masterPW

	return database['username'] !=''
	



def main():
	init()
	handleMainMenu()
	

def promptForNewUsername():
	return input('Enter an username:')

def promptForUsername():
	return input('Enter your username:')

def promptForManualGeneratedPassword():
	return input('Enter your new password:')

def validateMasterPassword(password):
	print(database)
	return password==database['masterPW']


def promptForNewMasterPassword():
	os.system('clear')
	return input('Enter a master password:')

def promptForMasterPassword():
	os.system('clear')
	return input('Enter your master password:')

def save_data(json_data):
    with open('database.json', 'w') as f:
        json.dump(json_data, f, indent=4)


def handleMainMenu():
	os.system('clear')
	print("*DEBUG***=-------"+database['username'])
	print("***********MainMenu***********")
	print("1) Password Vault")
	print("2) Change Master Password")
	print("3) Exit")

	option=input()

	if(option=='1'):
		os.system('clear')
		handlePasswordVault()
	if(option=='2'):
		print("noiiiice 2")
	if(option=='3'):
		 quit()


def handlePasswordVault():
	os.system('clear')
	print("***********PasswordVault***********")
	print("1) Secured Passwords")
	print("2) Add Password")
	print("3) Back")

	option=input()
	if(option == '1'):
		handleSecurePasswords()
	if(option=='2'):
		addNewPassword()
	if(option=='3'):
		handleMainMenu()


def addNewPassword():
	os.system('clear')
	passwordAlias=input("Enter the password alias: ")
	os.system('clear')
	handleNewPasswordMenu(passwordAlias)


def handleNewPasswordMenu(passwordAlias):
	os.system('clear')
	print("1) Genereate Password")
	print("2) Manual Password")
	print("3) Back")

	option=input()
	if(option == '1'):
		print("dfg")
	if(option=='2'):
		pw=promptForManualGeneratedPassword()
	if(option=='3'):
		handleMainMenu()
	newPW=SecuredPassword(passwordAlias,pw)


	database['securedPasswords'].append(newPW.toJson())

	print(database)
	save_data(database) # saving the json file
	##thelist[]



def handleSecurePasswords():
	os.system('clear')
	print("***********SecuredPasswords***********")
	
	for idx,item in enumerate(database["securedPasswords"]):
		daSON=json.loads(item)
		print(str(idx)+") "+daSON['alias'])

	print("6) Back")

	option=input()
	handleShowSecurePassword(option)

	if(option=='6'):
		handlePasswordVault()
	
	

def handleShowSecurePassword(number):
	os.system('clear')
	item=json.loads(database["securedPasswords"][int(number)])
	print("***********"+item['alias']+"*************")
	print(item['password'])
	print("*************************")
	print("1) Update")
	print("2) Delete")
	print("3) Back")

	option=input()

	if(option=='3'):
		handleSecurePasswords()


if __name__ == "__main__":
    main()
