#from gpsdata import *
import requests
import time
import json

def trip_init():
	comp=False
	while not comp:
		#location=loc()
		cur_time=time.strftime("%x %X")
		latitude="1.1"#(location[0])
		longitude="1.1"#(location[1])
		if latitude != "0.0" and longitude != "0.0":
			userdata={}
			userdata["uuid"]="107"
			userdata["vehicleid"]="101"
			gpsdata={}
			gpsdata["TimestampM"]=cur_time
			gpsdata["latitudeE7"]=15#latitude
			gpsdata["longitudeE7"]=15#longitude
			userdata["triplocation"]=gpsdata
			data=json.dumps(userdata)
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			resp = requests.post('http://lidsmysqldb.cloudapp.net/sih2017/lids-api/create.php', data=data,headers=headers,timeout=10)
			if resp.status_code==200:
				comp=True
	return cur_time
send_loc()
