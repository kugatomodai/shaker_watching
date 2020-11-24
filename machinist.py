import requests

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ${API_Key}'
}

data = '{"agent":"win10_shaker",
"metrics": [
{
"name": "0D",
"namespace": "OD_01",
"data_point": {
"value": 27.6
}
}
]
}'

response = requests.post('https://gw.machinist.iij.jp/endpoint', headers=headers, data=data)

"""
もとのやつ
api_key=<your_api_key>

curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ${api_key}" https://gw.machinist.iij.jp/endpoint -d @- << EOS
{
  "agent": "Home",
  "metrics": [
    {
      "name": "temperature",
      "namespace": "Environment Sensor",
      "data_point": {
        "value": 27.6
      }
    }
  ]
}
EOS
"""
