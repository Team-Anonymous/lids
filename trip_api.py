from gpsdata import *
import requests

def send_loc():
	comp=False
	while not comp:
		try:
			location=loc()
			latitude=(location[0])
			longitude=(location[1])
#			print(" "+latitude+" "+longitude)
			if latitude != "0.0" and longitude != "0.0":
				userdata = {'vehicle_id': "106", 'latitude': latitude, 'longitude': longitude}
				resp = requests.post('http://license.esy.es/insert.php', data=userdata,timeout=10)
				print(" "+location[0]+" "+location[1])
				print(resp.status_code)
				comp=True
		except:
			comp=True
			pass
