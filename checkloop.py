import os
import RPi.GPIO as GPIO
from time import sleep
from trip_register import *
from trip_update import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
comp=False
while not comp:
	x=os.popen("node card2.js").read().split('\n')
	if x[0] == "card removed":
		GPIO.output(23,GPIO.HIGH)
		GPIO.output(24,GPIO.LOW)
		GPIO.output(17,GPIO.LOW)
		print("Not available")
	else:
		db=pw.SqliteDatabase('admin')
		db.connect()
		cur=db.execute_sql("select * from admin_cards where id='%s'"%x[1])
		z=list(cur.fetchall())
		try:
			per=z[0][1]
		except:
			per=None
		if per=="add":
			GPIO.output(23,GPIO.LOW)
			GPIO.output(24,GPIO.HIGH)
			GPIO.output(17,GPIO.HIGH)
			print("Add card for addition")
			sleep(5)
			x=os.popen("node card2.js").read().split('\n')
			while x[0] == "card removed":
				x=os.popen("node card2.js").read().split('\n')
				continue
			cur=db.execute_sql("select * from admin_cards where id='%s';"%x[1])
			z=len(cur.fetchall())
			if z!=0:
				print("Card already registered")
			else:
				db.execute_sql("insert into admin_cards values('%s','access');"%x[1])
				print("Card Registered")
			for i in range(3):
				GPIO.output(17,GPIO.LOW)
				sleep(0.5)
				GPIO.output(17,GPIO.HIGH)
				sleep(0.5)
		elif per=="delete":
			GPIO.output(23,GPIO.HIGH)
			GPIO.output(24,GPIO.LOW)
			GPIO.output(17,GPIO.HIGH)
			print("Add card for deletion")
			sleep(2)
			x=os.popen("node card2.js").read().split('\n')
			while x[0] == "card removed":
				x=os.popen("node card2.js").read().split('\n')
				continue
			cur=db.execute_sql("select * from admin_cards where id='%s' and purpose='access';"%x[1])
			z=len(cur.fetchall())
			if z==0:
				print("Card not registered yet")
			else:
				for i in range(3):
					GPIO.output(17,GPIO.LOW)
					sleep(0.5)
					GPIO.output(17,GPIO.HIGH)
					sleep(0.5)
					db.execute_sql("delete from admin_cards where id='%s';"%x[1])
					print("Card Deleted")
		elif per=="access":
			istrip=True;
			init_time=0;
			GPIO.output(23,GPIO.LOW)
			GPIO.output(24,GPIO.HIGH)
			print("Card Accepted")
			x=os.popen("node card2.js").read().split('\n')
			while x[0] != "card removed":
				print("Sending location")
				if(istrip):
					init_time=trip_init()
				else:
					trip_cont(init_time)
					x=os.popen("node card2.js").read().split('\n')
					continue
		else:
			print("Card not registered")
 #   except:
#	GPIO.cleanup()
#	comp=True
