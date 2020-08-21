#importing modules
import mysql.connector
import random

#Creating Connetions
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="**********",
	database="**********"
)

mycursor = mydb.cursor()

#To Cretae Table
#mycursor.execute("CREATE TABLE Banking (name VARCHAR(255), phone VARCHAR(255), email VARCHAR(255), address VARCHAR(255), f_name VARCHAR(255), aadhar VARCHAR(255), pan VARCHAR(255), occu VARCHAR(255), balance VARCHAR(255),number VARCHAR(255), pin VARCHAR(255)) 



#To Create Account Number and pin
def create_account_number():
	number = ""
	pin = ""
	mycursor.execute("Select * FROM Banking")
	result = mycursor.fetchall()
	pin_list = [i[-1] for i in result]
	number_list =  [i[-2] for i in result]
	while True:
		#Creating a account number
		for i in range(10):
			number +=str(random.randint(0,9))
		#Checking if there is member who have same account number
		if number in number_list:
			number = ''
			continue
		else:
			break
	
	while True:
		#Creating A pin number
		for i in range(4):
			pin +=str(random.randint(0,9))
		#Checking if there is member who have same pin number
		if pin in pin_list:
			pin = ''
			continue
		else:
			break
	return number, pin
	
#to Add Member To Bank
def add_member(name, phone, email, address, f_name, aadhar, pan, occu):
	global mydb, mycursor
	number, pin = create_account_number() 
	mycursor.execute("INSERT INTO Banking (name, phone, email, address, f_name, aadhar, pan, occu, balance,number, pin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name, phone, email, address, f_name, aadhar, pan, occu, "0.0", number, pin ))
	mydb.commit()

#To Get Details of Last Person
def get_details():
	mycursor.execute('SELECT * FROM Banking ORDER BY id DESC LIMIT 1')
	result = mycursor.fetchall()
	return result[0]

#To Deposit Amount

def deposit(name, number, pin, amount):
	#Returns True if Payment is Successful else It Will Return False
	try:	
		#Checking Details Are Valid
		mycursor.execute(f"SELECT * FROM Banking WHERE number={number}")
		result = mycursor.fetchall()
		if len(result) == 0:
			return False
		
		if result[0][-1] == pin and result[0][1] == name:
			aleardy= result[0][-3]
			#Updating Account
			mycursor.execute(f"UPDATE Banking set balance = {float(aleardy) + round(float(amount))} WHERE number='{number}'")
			mydb.commit()
			return True
		else:
			return False
	except:
		return False

#To WithDraw Amount

def withdraw(name, number, pin, amount):
	#Returns True if Payment is Successful else It Will Return False
	try:	
		mycursor.execute(f"SELECT * FROM Banking WHERE number={number}")
		result = mycursor.fetchall()
		if len(result) == 0:
			return  "Invalid"
		if result[0][-1] == pin and result[0][1] == name:
			aleardy= result[0][-3]
			#Checking You Have Enough Money
			if float(aleardy)-round(float(amount))<0:
				return "Insufficient"
			#Updating Account
			mycursor.execute(f"UPDATE Banking set balance = {float(aleardy) - round(float(amount))} WHERE number='{number}'")
			mydb.commit()
			return "Done"
		else:
			return  "Invalid"
	except:
		return "Invalid"

# To Get Info Of Person
def get_info(name, number, pin):
	mycursor.execute(f"SELECT * FROM Banking WHERE number={number}")
	result = mycursor.fetchall()
	if len(result) == 0 or pin != result[0][-1] or name!=result[0][1]:
		return  (False, result[0])
	return (True, result[0])
	

if __name__ == "__main__":
	#TO Get All The Members Of Bank 
	mycursor.execute("SELECT * FROM Banking")
	result = mycursor.fetchall()
	for i in result:
		print(i) 
