import banking
from tkinter import *
from tkinter.messagebox import * 

class Main(Tk):
	def __init__(self):
		super().__init__()
	
		self.title("Bank")
		self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
		#Temparory Frame
		temp_frame  = Frame(self)
		temp_frame.place(x=0,y=0, relheight=1.0, relwidth=1.0)

		#This Is Frame Container Which HOld te the All Frame
		self.frame_cont = {}
		
		#Insert Frames in Frame Container
		for i in (MainFrame,Create, Deposit, Withdraw, Info):
			f = i(self, self)
			f.place(x=0,y=0, relheight=1.0, relwidth=1.0)
			self.frame_cont[i] = f
		self.show(self.frame_cont[MainFrame])
	#To show Frame
	def show(self, frame):
		frame.tkraise()
	
		

class MainFrame(Frame):
	#The Home Frame 
	def __init__(self, parent, controller):
		super().__init__(parent)
		Label(self, text="Welcome To \nDang's Bank", font="arial 25 bold").place(relx=0.35, rely=0, relwidth=0.3, relheight=1/6.5)		
		
		Button(self, text = "Create Account", font="arial 25 bold", relief=SOLID, command=lambda : controller.show(controller.frame_cont[Create])).place(relx = 0.35, rely=1/6, relwidth = 0.3, relheight=1/7)
		Button(self, text = "Account Statement", font="arial 25 bold", relief=SOLID, command=lambda : controller.show(controller.frame_cont[Info])).place(relx = 0.35, rely=2/6, relwidth=0.3, relheight=1/7)	
		Button(self, text = "Withdraw Money", font="arial 25 bold", relief=SOLID, command=lambda : controller.show(controller.frame_cont[Withdraw])).place(relx = 0.35 , rely=3/6, relwidth=0.3, relheight=1/7)
		Button(self, text = "Deposit Money", font="arial 25 bold", relief=SOLID, command=lambda : controller.show(controller.frame_cont[Deposit])).place(relx = 0.35, rely=4/6, relwidth=0.3, relheight=1/7)

		

class Create(Frame):
	#The New Member Page
	def __init__(self, parent, controller):
		super().__init__(parent)
		Label(self, text="Create Account", font="arial 50 bold").place(relx=0.3, rely=0, relwidth=0.4, relheight=1/6)

		Label(self, text="Name:-", font="arial 25 bold").place(relx=0.01, rely=1/6, relwidth=0.21, relheight=1/6)
		self.name = StringVar()
		Entry(self, textvariable=self.name, font="arial 20 ", relief="sunken", bd="5").place(relx=0.24,rely=7/32, relwidth=0.21, relheight=1/16)
			
		Label(self, text="Phone:-", font="arial 25 bold").place(relx=0.01, rely=2/6, relwidth=0.2, relheight=1/6)
		self.number = StringVar()
		Entry(self, textvariable=self.number, font="arial 20 ", relief="sunken", bd="5").place(relx=0.24, rely=7/32 + 1/6, relwidth=0.21, relheight=1/16)

		Label(self, text="Email:-", font="arial 25 bold").place(relx=0.01, rely=3/6, relwidth=0.2, relheight=1/6)
		self.email = StringVar()
		Entry(self, textvariable=self.email, font="arial 20 ", relief="sunken", bd="5").place(relx=0.24, rely=7/32 + 2/6, relwidth=0.21, relheight=1/16)
	
		Label(self, text="Address:-", font="arial 25 bold").place(relx=0.01, rely=4/6, relwidth=0.2, relheight=1/6)
		self.add = Text(self, font="arial 20 ", relief="sunken", bd="5")
		self.add.place(relx=0.24, rely=7/32 + 3/6, relwidth=0.21, relheight=1/8)


	
		Label(self, text="F. Name:-", font="arial 25 bold").place(relx=0.47, rely=1/6, relwidth=0.21, relheight=1/6)
		self.f_name = StringVar()
		Entry(self, textvariable=self.f_name, font="arial 20 ", relief="sunken", bd="5").place(relx=0.70,rely=7/32, relwidth=0.21, relheight=1/16)	
		
		Label(self, text="Aadhar:-", font="arial 25 bold").place(relx=0.47, rely=2/6, relwidth=0.21, relheight=1/6)
		self.aadhar = StringVar()
		Entry(self, textvariable=self.aadhar, font="arial 20 ", relief="sunken", bd="5").place(relx=0.70,rely=7/32 + 1/6, relwidth=0.21, relheight=1/16)	
	
		Label(self, text="Occupation:-", font="arial 25 bold").place(relx=0.47, rely=3/6, relwidth=0.21, relheight=1/6)
		self.occu = StringVar()
		Entry(self, textvariable=self.occu, font="arial 20 ", relief="sunken", bd="5").place(relx=0.70,rely=7/32+2/6, relwidth=0.21, relheight=1/16)
		
		Label(self, text="PAN No.:-", font="arial 25 bold").place(relx=0.47, rely=4/6, relwidth=0.21, relheight=1/6)
		self.pan = StringVar()
		Entry(self, textvariable=self.pan, font="arial 20 ", relief="sunken", bd="5").place(relx=0.70,rely=7/32+3/6, relwidth=0.21, relheight=1/16)
		
		#Submit The details and back Button
		Button(self, text="Submit", font="arial 25 bold", relief="raised", bd="5", command=self.check).place(relx=0.4, rely=7/8, relheight=1/8, relwidth=0.2)	
		Button(self, text="Back", font="arial 15 bold", relief="sunken", bd=2, command=lambda: self.Back(controller)).place(relx=0.1, rely=7.5/8)
	
	#To Go Back
	def Back(self, controller):
		self.reset()
		controller.show(controller.frame_cont[MainFrame])

	def check(self):
		#Checking id There Any Non-filled Entry
		for i in (self.name, self.number, self.email, self.f_name, self.aadhar, self.occu, self.pan):
			if i.get().replace(" ", "")=="":
				showerror("Error", "Please provide us full information")	
				return
				break
				
		#Validating Email
		if "@" not in self.email.get() or "." not in self.email.get():
			showerror("Error", "Enter Valid Email Address")
			return
		self.submit()
	
	def submit(self):
		#Submiting the Form
		banking.add_member(self.name.get(), self.number.get(),self.email.get(), self.add.get(1.0, END),self.f_name.get(), self.aadhar.get(), self.pan.get(), self.occu.get() )
		self.success()
	
	def reset(self):
		#Reseting All Entry
		self.name.set("")
		self.number.set("")
		self.email.set("")
		self.add.delete(1.0, END)
		self.f_name.set("")
		self.aadhar.set("")
		self.pan.set("")
		self.occu.set("")
		
	def success(self):
		#Showing theb Success And Details
		global controller 
		self.reset()
		result = banking.get_details()
		top = Toplevel(width=500, height=300)
		top.resizable(0,0)
		
		Label(top, text="Success", font="arial 25 bold").place(relx=0.25, rely=0, relwidth=0.5, relheight=0.1)
		Label(top, text = f"Name: {result[1]}", font="arial 20 bold").place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)
		Label(top, text = f"Uniqe ID: {result[0]}", font="arial 20 bold").place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.1)
		Label(top, text = f"PIN: {result[-1]}", font="arial 20 bold").place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.1)
		Label(top, text = f"Acount Number: {result[-2]}", font="arial 20 bold").place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

		top.mainloop()
	
				
class 	Deposit(Frame):
	#Deposit Frame
	def __init__(self, parent, controller):
		super().__init__(parent)
		Label(self, text="Deposit", font="arial 40 bold").place(relx=0.3, rely=0, relwidth=0.4, relheight=1/6)
		
		Label(self, text="Name:", font="verdana 30 bold").place(relx=0.1, rely=1/6, relwidth=0.4, relheight=1/6)
		self.name = StringVar()
		Entry(self, textvariable=self.name, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 1/6, relwidth=0.4, relheight=1/16)

		Label(self, text="PIN:", font="verdana 30 bold").place(relx=0.1, rely=2/6, relwidth=0.4, relheight=1/6)
		self.pin = StringVar()
		Entry(self, textvariable=self.pin, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 2/6, relwidth=0.4, relheight=1/16)

		Label(self, text="Account Number:", font="verdana 30 bold").place(relx=0.1, rely=3/6, relwidth=0.4, relheight=1/6)
		self.number = StringVar()
		Entry(self, textvariable=self.number, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 3/6, relwidth=0.4, relheight=1/16)

		Label(self, text="Amount", font="verdana 30 bold").place(relx=0.1, rely=4/6, relwidth=0.4, relheight=1/6)
		self.amount = StringVar()
		Entry(self, textvariable=self.amount, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 4/6, relwidth=0.4, relheight=1/16)
	
		Button(self, text="Deposit", font="verdana 30 bold", relief="raised", bd=4, command=self.deposit_).place(relx=0.35, rely=5/96 + 4/6+1/8, relwidth=0.3, relheight=1/8)
		Button(self, text="Back", font="arial 15 bold", relief="sunken", bd=2, command=lambda : self.Back(controller)).place(relx=0.1, rely=7.5/8)

	#To Go Back
	def Back(self, controller):
		self.reset()
		controller.show(controller.frame_cont[MainFrame])



	def deposit_(self):
		#Updating The Database
		if banking.deposit(self.name.get(), self.number.get(), self.pin.get(), float(self.amount.get())):
			showinfo("Bank", "You'r Money Is Deposited To Your Account")
		else:
			showerror("Bank", "Please Provide Right Information")
		self.reset()
	def reset(self):
		#To Reset entries
		self.name.set("")
		self.number.set("")
		self.pin.set("")
		self.amount.set("")

class Withdraw(Frame):
	#Withdrawing Frame
	def __init__(self, parent, controller):
		super().__init__(parent)
		Label(self, text="Withdraw", font="arial 40 bold").place(relx=0.3, rely=0, relwidth=0.4, relheight=1/6)
		
		Label(self, text="Name:", font="verdana 30 bold").place(relx=0.1, rely=1/6, relwidth=0.4, relheight=1/6)
		self.name = StringVar()
		Entry(self, textvariable=self.name, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 1/6, relwidth=0.4, relheight=1/16)

		Label(self, text="PIN:", font="verdana 30 bold").place(relx=0.1, rely=2/6, relwidth=0.4, relheight=1/6)
		self.pin = StringVar()
		Entry(self, textvariable=self.pin, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 2/6, relwidth=0.4, relheight=1/16)

		Label(self, text="Account Number:", font="verdana 30 bold").place(relx=0.1, rely=3/6, relwidth=0.4, relheight=1/6)
		self.number = StringVar()
		Entry(self, textvariable=self.number, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 3/6, relwidth=0.4, relheight=1/16)

		Label(self, text="Amount", font="verdana 30 bold").place(relx=0.1, rely=4/6, relwidth=0.4, relheight=1/6)
		self.amount = StringVar()
		Entry(self, textvariable=self.amount, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 4/6, relwidth=0.4, relheight=1/16)
	
		Button(self, text="Withdraw", font="verdana 30 bold", relief="raised", bd=4, command=self.withdraw_).place(relx=0.35, rely=5/96 + 4/6+1/8, relwidth=0.3, relheight=1/8)
		Button(self, text="Back", font="arial 15 bold", relief="sunken", bd=2, command=lambda : self.Back(controller)).place(relx=0.1, rely=7.5/8)
		
	#To Go Back
	def Back(self, controller):
		self.reset()
		controller.show(controller.frame_cont[MainFrame])


	def reset(self):
		self.name.set("")
		self.number.set("")
		self.pin.set("")
		self.amount.set("")

	def withdraw_(self):
		#To Update The Database
	
	
		results =  banking.withdraw(self.name.get(), self.number.get(), self.pin.get(), float(self.amount.get())) 	
		if results== "Done":
			showinfo("Bank", "You'r Money Is Withdraw From Your Account")
			self.reset()
			return
		elif results == "Invalid" :
			showerror("Bank", "Please Provide Right Information")
			return
		else:
			showerror("Bank", "You Doesn't Have Enough Money.")

			

class Info(Frame):
	#Information Frame
	def __init__(self, parent, controller):
		super().__init__(parent)
		Label(self, text="Account Details", font="arial 40 bold").place(relx=0.3, rely=0, relwidth=0.4, relheight=1/6)
		
		Label(self, text="Name:", font="verdana 30 bold").place(relx=0.1, rely=1/6, relwidth=0.4, relheight=1/6)
		self.name = StringVar()
		Entry(self, textvariable=self.name, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 1/6, relwidth=0.4, relheight=1/16)

		Label(self, text="PIN:", font="verdana 30 bold").place(relx=0.1, rely=2/6, relwidth=0.4, relheight=1/6)
		self.pin = StringVar()
		Entry(self, textvariable=self.pin, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 2/6, relwidth=0.4, relheight=1/16)

		Label(self, text="Account Number:", font="verdana 30 bold").place(relx=0.1, rely=3/6, relwidth=0.4, relheight=1/6)
		self.number = StringVar()
		Entry(self, textvariable=self.number, font="verdana 30 bold").place(relx=0.5, rely=5/96 + 3/6, relwidth=0.4, relheight=1/16)

			
		Button(self, text="Submit", font="verdana 30 bold", relief="raised", bd=4, command=self.get_info_).place(relx=0.35, rely=5/96 + 4/6+1/8, relwidth=0.3, relheight=1/8)
		Button(self, text="Back", font="arial 15 bold", relief="sunken", bd=2, command=lambda : self.Back(controller)).place(relx=0.1, rely=7.5/8)	
	#To Go Back
	def Back(self, controller):
		self.reset()
		controller.show(controller.frame_cont[MainFrame])

	def get_info_(self):
		#To Get Info
		result  = banking.get_info(self.name.get(), self.number.get(), self.pin.get())
		if result[0]:
			self.show_info(result[1])
		else:
			showerror("Bank", "Invalid Information")
	def reset(self):
		self.name.set("")
		self.number.set("")
		self.pin.set("")
	def show_info(self, result):
		#Showing Info


		top = Toplevel(width=500, height=300)
		top.resizable(0,0)
		
		Label(top, text="Account Information", font="arial 25 bold").place(relx=0.15, rely=0, relwidth=0.7, relheight=0.1)
		Label(top, text = f"Name: {result[1]}", font="arial 20 bold").place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)
		Label(top, text = f"Uniqe ID: {result[0]}", font="arial 20 bold").place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.1)
		Label(top, text = f"Balance: {result[-3]}", font="arial 20 bold").place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.1)
		Label(top, text = f"Account Number: {result[-2]}", font="arial 20 bold").place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)
		

		top.mainloop()
	
	
if __name__ == "__main__":
	game = Main()
	game.mainloop()
