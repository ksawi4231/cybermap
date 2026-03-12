import requests
import json
import random
import time

wszystkie_ataki = []
wszytkie_miasta = []
lista_odpowiedzi=[]
x=[]
y=[]

with open('miasta_lokalizacja.json', 'r') as file1:
    miasta = json.load(file1)

for i in miasta['cities']:
    wszytkie_miasta.append(i)

url = 'https://api.abuseipdb.com/api/v2/blacklist'

querystring = {'confidenceMinimum':'90', 'limit': '15'}

headers = {
    'Accept': 'application/json',
    'Key': '85a3db26ce572ebf950ec258f5d36a9f46e38899fa62c85e00ae8b0c95141c65289ef164e3c251b0'
}

baza_danych = requests.request(method='GET', url=url, headers=headers, params=querystring).json()

for i in baza_danych['data']:
    odpowiedz = requests.get(f"http://ip-api.com/json/{i['ipAddress']}")
    lista_odpowiedzi.append(odpowiedz.json())
    time.sleep(1.5)


for i in lista_odpowiedzi:
    x.append(i['lat'])
    y.append(i['lon'])

licznik=0

for i in baza_danych['data']:
    
    cel = random.choice(wszytkie_miasta)
    atak = {
        "startLat": x[licznik],
        "startLng": y[licznik],
        "endLat": cel['lat'],
        "endLng": cel['lng'],
    }
    wszystkie_ataki.append(atak)
    licznik+=1

with open('attacks.json', 'w') as f:
    json.dump(wszystkie_ataki, f, indent=4)
