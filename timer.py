import time
from tkinter import *
from tkinter import StringVar
class clock:
	def __init__(self,value):
		self.value = value
		main = Tk()
		main.geometry('300x300')
		main.title("Timer")
		self.currenttime = time.localtime()
		self.currenthour=self.currenttime.tm_hour
		self.currentmin = self.currenttime.tm_min
		self.target = {"H":0,"M":0,"S":0} 
		self.countdownlabeltext = StringVar()
		self.countdownlabeltext.set("{}:{}:{}".format(self.target['H'],self.target['M'],self.target['S']))
		self.countdownlabel = Label(main,textvariable = self.countdownlabeltext ,font=("Ubuntu Bold",30))
		self.thourslabel = Label(main,text="Hour : ")
		self.tminslabel = Label(main,text="Min : ")
		self.tsecslabel = Label(main,text="Sec : ")

		setbut = Button(main,text= "set", command = self.setvalue)
		startbut = Button(main,text="start")
		pausebut=Button(main, text= "sart")#,command = self.)
		stopbut=Button(main, text= "sart")#,command = self.)


		self.thourentry= Entry(main)
		self.tminentry= Entry(main)
		self.tsecentry= Entry(main)

		self.countdownlabel.grid(row=0,column=0,columnspan=3,sticky=E+W)

		self.thourslabel.grid(row=1,column=0,sticky=E)
		self.thourentry.grid(row=1,column=1,columnspan = 2,sticky=E)
		self.tminslabel.grid(row=2,column=0,sticky=E)
		self.tminentry.grid(row=2,column=1,columnspan = 2,sticky=E)
		self.tsecslabel.grid(row=3,column=0,sticky=E)
		self.tsecentry.grid(row=3,column=1,columnspan = 2,sticky=E)


		startbut.grid(row =5,column = 0 , sticky = E + W)
		setbut.grid(row=4,column=0,columnspan=3,sticky=E+W)
		pausebut.grid(row =5 , column = 1, sticky = E + W)
		stopbut.grid(row =5 , column = 2, sticky = E + W)


		main.mainloop()


	def get(self):
		# self.target['H'] = self.thourentry.get()
		# self.target['M'] = self.tminentry.get()
		# self.target['S'] = self.tsecentry.get()
		try:
			self.target['H'] = int(self.thourentry.get())
			if self.target['H'] == "":
				self.target['H'] == 0
		except ValueError:
			self.target['H'] = 0
			self.thourentry.delete(0)
			self.thourentry.insert(0,"Please enter a number")
		try:
			self.target['M'] = int(self.tminentry.get())
			if self.target['M'] == "":
				self.target['M'] == 0
		except ValueError:
			self.target['M'] = 0
			self.tminentry.delete(0)
			self.tminentry.insert(0,"Please enter a number")
		try:
			self.target['S'] = int(self.tsecentry.get())
			if self.target['S'] == "":
				self.target['S'] == 0
		except ValueError:
			self.target['S'] = 0
			self.tsecentry.delete(0)
			self.tsecentry.insert(0,"Please enter a number")

		
	def setvalue(self):
		self.get() 
		self.countdownlabeltext.set("{}:{}:{}".format(self.target['H'],self.target['M'],self.target['S']))
	def start(self):
		self.get()
		mincount =0
		hourcount = 0
		seccount = 0
		while self.target['S'] >= 0:
			self.target['S'] -= 1
			seccount += 1
			time.sleep(1)
			if seccount == 60 and self.target['M'] >= 0 :
				self.target['M'] -= 1 
				mincount += 1
				seccount = 0
			if mincount ==60 and self.target['H'] >= 0:
				self.target['H'] -= 1
				hourcount += 1
				mincount = 0








clock(20)