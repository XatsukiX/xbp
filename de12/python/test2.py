import requests
import json

url="https://api.openweathermap.org/data/2.5/forecast?q={city}&appid{key}&lang=ja&units=metric"
url= url.format(city="Yokohama,JP",key="bad5e934d78a420d7cae96a961a93508")

jsondata = requests.get(url).json()
print(jsondata)