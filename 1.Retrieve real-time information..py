import requests, json
url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'

data = requests.get(url).json()

for i in data['records']:

  print(i['county'] + ' ' + i['sitename'], end='，')    
  print('AQI:' + i['aqi'], end='，')                    
  print('空氣品質:' + i['status'])