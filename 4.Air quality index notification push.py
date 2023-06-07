import requests, json

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

url1 = "https://notify-api.line.me/api/notify"
headers = {
    "Authorization": "Bearer " + token, 
    "Content-Type" : "application/x-www-form-urlencoded"
}

url2 = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data = requests.get(url2).json()

### a = input("城市") 
a = "臺南市"
### b = input("站名") 
b = "臺南"

for i in data['records']:

  if i['county'] == "臺南市" and i['sitename'] == "臺南" :

    x = i['aqi']
    y = i['status']

z = "\n\nAQI : " + x +"\n\n空氣品質 : " + y
print(z)

msg = z
payload = {'message': msg}
r = requests.post(url1, headers = headers, params = payload)
print(r)