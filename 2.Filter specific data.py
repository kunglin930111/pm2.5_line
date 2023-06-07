import requests, json
url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'

data = requests.get(url).json()

### a = input("城市") a = "臺南市"
### b = input("站名") b = "臺南"

for i in data['records']:

    if i['county'] == "臺南市" and i['sitename'] == "臺南" :
      x = i['aqi'] + " " + i['status']

print(x)
