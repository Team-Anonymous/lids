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
        poll_data["startdate"]=time.strftime('%Y-%m-%d')
        data=json.dumps(poll_data)
        print(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        resp = requests.post('http://lidsmysqldb.cloudapp.net/sih2017/lids-api/CFinsert.php', data=data,headers=headers,timeout=10)
        if resp.status_code==200:
            comp=True
