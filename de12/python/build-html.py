import requests
import codecs

url="https://xatsukix.github.io/xbp/de12/4.html"
response = requests.get(url)



filename = "download.html"
with open(filename, mode="w", encoding="utf-8") as f:

 f.write(response.text )

