import requests
import json
import random

wszystkie_ataki = []
wszytkie_miasta = []

with open('testowe_ip.json', 'r') as file1:
    data = json.load(file1)

with open('miasta_lokalizacja.json', 'r') as file2:
    miasta = json.load(file2)

for i in miasta['cities']:
    wszytkie_miasta.append(i)

#url = 'https://api.abuseipdb.com/api/v2/blacklist'

#querystring = {'confidenceMinimum':'90'}

#headers = {
    #'Accept': 'application/json',
   #'Key': '85a3db26ce572ebf950ec258f5d36a9f46e38899fa62c85e00ae8b0c95141c65289ef164e3c251b0'
#}

# = requests.request(method='GET', url=url, headers=headers, params=querystring)

#dane = response.json()

for i in data['data']:
    ip=i['ipAddress']
    lokalizacja = requests.get(f'http://ip-api.com/json/{ip}').json()
    if lokalizacja['status'] == 'success':
        cel = random.choice(wszytkie_miasta)
        atak = {
            "startLat": lokalizacja['lat'],
            "startLng": lokalizacja['lon'],
            "endLat": cel['lat'],
            "endLng": cel['lng'],
            "ip": ip,
        }
        wszystkie_ataki.append(atak)

with open('attacks.json', 'w') as f:
    json.dump(wszystkie_ataki, f, indent=4)
