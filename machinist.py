import urllib.request
import json
import time
APIKEY = "xxxxxx"
Url = "https://gw.machinist.iij.jp/endpoint"
method = "POST"
 
def sendMachinist(name, pv):
    data = {
        "agent": "win10_sensor",
        "metrics": [
            {
                "name": name,
                "namespace": "OD_sensor",
                "data_point": {
                    "value": pv
                }
            }
        ]
    }
 
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + APIKEY,
        "User-Agent": "Python3"
    }
 
    senddata = json.dumps(data).encode("ascii")
    req = urllib.request.Request(Url, data=senddata, method=method, headers=headers)
    with urllib.request.urlopen(req) as res:
        html = res.read().decode("ascii")
        if "Succeeded" in html:
        print("send OK")
 
i = 2
for sdata in range(10):
    sendMachinist(sdata+i*3);
    time.sleep(10);
