import numpy as np
import pandas as pd
from datetime import datetime
import csv
import sys
# influxdb_client　APIを利用
from influxdb_client import InfluxDBClient, Point, WritePrecision, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS


# You can generate a Token from the "Tokens Tab" in the UI
token = "xxx"
org = "xxx"
bucket = "xxx"

client = InfluxDBClient(url="xxx", token=token)


def load_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        
    df = pd.DataFrame(l[12:])
    df.columns = ['Timestamp', 'time','OD_01', 'OD_02', 'OD_03', 'OD_04', 'OD_05', 'OD_06', 'OD_07', 'OD_08', 'temp']
    # df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df_2 = df.tail(1)
    col = list(df_2)
    
    # value dtypes to float
    for i in col[2:10]:
        df_2[i] = pd.to_numeric(df_2[i])
    
    # dtype of timestamp to datetime
    df_2['Timestamp'] = pd.to_datetime(df_2['Timestamp'])
    print(df_2)
    
    ## Write Pandas DataFrame
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()
    
    data_frame = pd.DataFrame(data=[["OD_01", df_2.iat[0, 2]], ["OD_02", df_2.iat[0, 3]], ["OD_03", df_2.iat[0, 4]], ["OD_04", df_2.iat[0, 5]], ["OD_05", df_2.iat[0, 6]], ["OD_06", df_2.iat[0, 7]], ["OD_07", df_2.iat[0, 8]], ["OD_08", df_2.iat[0, 9]]],
                           index=[datetime.utcnow(), datetime.utcnow(), datetime.utcnow(), datetime.utcnow(), datetime.utcnow(), datetime.utcnow(), datetime.utcnow(), datetime.utcnow()],
                           columns=["sensor", "PV"])
    print(df_2.iat[0, 0])
    print(datetime.utcnow())
    write_api.write(bucket, org, record=data_frame, data_frame_measurement_name='mea1',
                    data_frame_tag_columns=['sensor'])
                    
    ## Close client
    write_api.__del__()
    client.__del__()

# execute with target file name
if __name__ == "__main__":
    load_data(sys.argv[1])



