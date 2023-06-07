import requests

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
url = "https://notify-api.line.me/api/notify"
headers = {
    "Authorization": "Bearer " + token, 
    "Content-Type" : "application/x-www-form-urlencoded"
}

msg = 'test'

payload = {'message': msg}
r = requests.post(url, headers = headers, params = payload)
print(r)