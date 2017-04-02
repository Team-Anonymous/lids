from gpsdata import *
import requests
import time
import json
from datetime import datetime

def trip_cont(start_time,flag,tripid):
	comp=False
	while not comp:
		location=loc()
		dt=datetime.now()
		cur_time=int(time.mktime(dt.timetuple()))
		latitude=(location[0])
		longitude=(location[1])
		if latitude != "0.0" and longitude != "0.0":
			userdata={}
			userdata["tripid"]=tripid
			userdata["uuid"]="109"
			userdata["vehicleid"]="104"
			userdata["timestampMs"]=cur_time
			userdata["duration"]=cur_time-start_time
			userdata["latitudeE7"]=latitude
			userdata["longitudeE7"]=longitude
			userdata["istriplive"]=flag;
			data=json.dumps(userdata)
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			resp = requests.post('http://lidsmysqldb.cloudapp.net/sih2017/lids-api/updateTrip.php', data=data,headers=headers,timeout=10)
			if resp.status_code==200:
				comp=True
	if flag:
		return cur_time-start_time;
