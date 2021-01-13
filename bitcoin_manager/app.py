import requests

url = "http://api.bitcoincharts.com/v1/markets.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)