import pandas as pd
import csv
import sys
from datetime import datetime
import urllib.request
import json
import time
APIKEY = "xxx"
Url = "https://gw.machinist.iij.jp/endpoint"
method = "POST"


def sendMachinist(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        
    df = pd.DataFrame(l[12:])
    df.columns = ['Timestamp', 'time','OD_01', 'OD_02', 'OD_03', 'OD_04', 'OD_05', 'OD_06', 'OD_07', 'OD_08', 'temp']
    df_2 = df.tail(1)
    col = list(df_2)
    
    # value dtypes to float
    for i in range(2, 10):
        name = col[i]
        pv = float(df_2.iat[0, i])


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
                print("send OK "+ name)

if __name__ == "__main__":
    sendMachinist(sys.argv[1])

