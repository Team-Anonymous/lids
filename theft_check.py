import requests
import time
import json

def stop_command(vehicle_id):
    theft=False
    userdata={}
    userdata["vehicle_id"]=vehicle_id
    data=json.dumps(userdata)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.post('http://lidsmysqldb.cloudapp.net/sih2017/lids-api/immobilizer.php', data=data,headers=headers,timeout=10)
    if resp.status_code==200:
        getdata=json.loads(resp.content.decode('utf-8'))
        if(getdata["Immobilized"]):
            theft=True
    return theft
