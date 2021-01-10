import requests

url = "http://api.bitcoincharts.com/v1/markets.json"

response = requests.request("GET", url)

print(response.text)