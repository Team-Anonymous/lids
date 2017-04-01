import requests
import time
import json

EFactor=0.18

def poll_count(vehicleid,duration):
    comp=False
    while not comp:
        cf=duration*EFactor
        poll_data={}
        poll_data["cf"]=cf
        poll_data["licenseid"]=vehicleid
        poll_data["start_date"]=time.strftime('%x')
        data=json.dumps(poll_data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        resp = requests.post('http://lidsmysqldb.cloudapp.net/sih2017/lids-api/CFinsert.php', data=data,headers=headers,timeout=10)
        if resp.status_code==200:
            getdata=resp.json()
            trip_id=resp["tripid"]
            comp=True
        comp=True
