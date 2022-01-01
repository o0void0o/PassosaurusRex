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
	os.system('clear')
	return input('Enter your new manual password:')

def promptForManualGeneratedPasswordConfirm():
	os.system('clear')
	return input('Confirm manual password:')


def validateMasterPassword(password):
	print(database)
	assert password==database['masterPW']

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

	print("*********** Main Menu ***********")
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
		handleSecurePasswordsMenu()
	if(option=='2'):
		addNewSecuredPassword()
	if(option=='3'):
		handleMainMenu()

def addNewSecuredPassword():
	passwordAlias = promptForAlias()
	pw = handleNewPasswordMenu(passwordAlias,'')

	newPW =  SecuredPassword(passwordAlias,pw)
	database['securedPasswords'].append(newPW.toJson())

	print(database)
	save_data(database) # saving the json file

	handleSavedNewSecuredPasswordMenu(passwordAlias)



def handleSavedNewSecuredPasswordMenu(passwordAlias):
	os.system('clear')
	print("***********"+passwordAlias +" saved***********")
	print("1) View Secueurd passwords")
	print("2) Main Menu")

	option=input()
	if(option == '1'):
		handleSecurePasswordsMenu()
	else:
		handleMainMenu()

	
def promptForAlias():
	os.system('clear')
	return input("Enter the password alias: ")	


def handleNewPasswordMenu(passwordAlias,mesg):
	os.system('clear')
	if mesg!='':
		print("****************************")
		print(mesg)
		print("****************************")

	
	print("1) Genereate Password")
	print("2) Manual Password")
	print("3) Back")

	option=input()
	if(option == '1'):
		print("dfg")
	if(option=='2'):
		pw=promptForManualGeneratedPassword()
		pw2=promptForManualGeneratedPasswordConfirm()

		if pw !=pw2:
			handleNewPasswordMenu(passwordAlias,"Provdided passwords dont match")

	if(option=='3'):
		handleMainMenu()

	return pw


	



def handleSecurePasswordsMenu():
	os.system('clear')
	print("*********** Secured Passwords ***********")
	
	for idx,item in enumerate(database["securedPasswords"]):
		daSON=json.loads(item)
		print(str(idx)+") "+daSON['alias'])

	print("")
	print("x) Main Menu")


	option=input()

	if(option=='x'):
		handlePasswordVault()


	handleShowSecurePassword(option)



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
		handleSecurePasswordsMenu()


if __name__ == "__main__":
    main()
