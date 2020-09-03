import time
from tkinter import *
from tkinter import StringVar #this is to change the timer label for each second using variable string
class clock:
	def __init__(self,value):
		self.value = value
		self.main = Tk()
		self.main.geometry('300x300')
		self.main.title("Timer")
		self.target_time = {"H":0,"M":0,"S":0} 
		self.countdownlabeltext = StringVar()
		self.countdownlabeltext.set("{}:{}:{}".format(self.target_time['H'],self.target_time['M'],self.target_time['S']))
		self.countdownlabel = Label(self.main,text = self.countdownlabeltext.get() ,font=("Ubuntu Bold",30))
		self.thourslabel = Label(self.main,text="Hour : ")
		self.tminslabel = Label(self.main,text="Min : ")
		self.tsecslabel = Label(self.main,text="Sec : ")

		setbut = Button(self.main,text= "set", command = self.setvalue)
		startbut = Button(self.main,text="start",command = self.start)
		pausebut=Button(self.main, text= "pause")#,command = self.)
		stopbut=Button(self.main, text= "stop")#,command = self.)


		self.thourentry= Entry(self.main)
		self.tminentry= Entry(self.main)
		self.tsecentry= Entry(self.main)

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

		
		self.main.mainloop()


	def get(self):
		try:
			self.target_time['H'] = int(self.thourentry.get())
			if self.target_time['H'] == "":
				self.target_time['H'] == 0
		except ValueError:
			self.target_time['H'] = 0
			self.thourentry.delete(0)
			self.thourentry.insert(0,"Please enter a number")
		try:
			self.target_time['M'] = int(self.tminentry.get())
			if self.target_time['M'] == "":
				self.target_time['M'] == 0
		except ValueError:
			self.target_time['M'] = 0
			self.tminentry.delete(0)
			self.tminentry.insert(0,"Please enter a number")
		try:
			self.target_time['S'] = int(self.tsecentry.get())
			if self.target_time['S'] == "":
				self.target_time['S'] == 0
		except ValueError:
			self.target_time['S'] = 0
			self.tsecentry.delete(0)
			self.tsecentry.insert(0,"Please enter a number")

		
	def setvalue(self):
		self.get() 
		self.countdownlabeltext.set("{}:{}:{}".format(self.target_time['H'],self.target_time['M'],self.target_time['S']))
		self.countdownlabel.configure(text=self.countdownlabeltext.get())
	
	def start(self):
		totalseconds = (self.target_time['H']*3600) + (self.target_time['M']*60) + self.target_time['S']
		while True:
			totalseconds -= 1
			# seccount += 1
			self.target_time['S'] = totalseconds % 60 
			self.target_time['M'] = int(totalseconds / 60)

			if self.target_time['M'] >=60:

				self.target_time['H'] = int(totalseconds/3600)
				self.target_time['M'] = (int(totalseconds /60))%60

			if totalseconds == 0:
				break

			self.update()
			time.sleep(1)

	def update(self):	
		h = self.target_time['H']
		m = self.target_time['M']
		s = self.target_time['S']
		
		self.countdownlabeltext.set("{}:{}:{}".format(h,m,s))

		
		self.countdownlabel.configure(text=self.countdownlabeltext.get())
		self.main.update()






clock(20)