from gpsdata import *
import requests
import time
import json

def trip_init():
	comp=False
	trip_id=0
	while not comp:
		location=loc()
		cur_time=int(time.time())
		latitude=(location[0])
		longitude=(location[1])
		if latitude != "0.0" and longitude != "0.0":
			userdata={}
			userdata["uuid"]="107"
			userdata["vehicleid"]="101"
			userdata["timestampMs"]=cur_time
			userdata["latitudeE7"]=latitude
			userdata["longitudeE7"]=longitude
			data=json.dumps(userdata)
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			resp = requests.post('http://lidsmysqldb.cloudapp.net/sih2017/lids-api/createTrip.php', data=data,headers=headers,timeout=10)
			if resp.status_code==200:
				getdata=json.loads(resp.content.decode('utf-8'))
				trip_id=getdata["tripid"]
				comp=True
	return cur_time,trip_id
