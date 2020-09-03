import time
import os 

target = dict()

while True:

	try:
		target['h']= int(input("Enter the number of hours : "))
		target['m']= int(input("Enter the number of minutes : "))
		target['s']= int(input("Enter the number of seconds : "))
		break
	except ValueError:
		print("try again !")

totalseconds = target['h']*3600 + target['m']*60 + target['s']
input("Press Any Key to Start the Countdown !")

while True:
	totalseconds -=1
	target['s'] = totalseconds%60
	target['m'] = int(totalseconds/60)

	if target['m'] >= 60:
		target['h'] = int(totalseconds/3600)
		target['m'] = int(totalseconds/60)%60
	print("Hour: ", target['h'])
	print("Minutes: ", target['m'])
	print("Seconds: ", target['s'])
	if totalseconds ==0:
		break
	os.system('clear')
	time.sleep(1)