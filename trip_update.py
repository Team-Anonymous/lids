#from gpsdata import *
import requests
import time
import json

def trip_cont(start_time,flag):
	comp=False
	while not comp:
		location=loc()
		cur_time=time.strftime("%x %X")
		latitude=(location[0])
		longitude=(location[1])
		if latitude != "0.0" and longitude != "0.0":
			userdata={}
			userdata["uuid"]="107"
			userdata["vehicleid"]="101"
			userdata["TimestampMS"]=cur_time-start_time
			userdata["latitudeE7"]=latitude
			userdata["longitudeE7"]=longitude
			userdata["isTripLive"]=flag;
			data=json.dumps(userdata)
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			resp = requests.post('http://lidsmysqldb.cloudapp.net/sih2017/lids-api/create.php', data=data,headers=headers,timeout=10)
			if resp.status_code==200:
				comp=True
