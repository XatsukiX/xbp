import requests
from bs4 import BeautifulSoup
import urllib
import codecs

url = "https://www.yahoo.co.jp/l"
html = requests.get(url)
soup = BeautifulSoup(html.content,"html.parser")

filename = "linklist.text"
with open(filename,"w", encoding="utf-8") as f:

    topic = soup.find(class_="_2DunygeBZHdgHX_Gih3GC4")
    for element in topic.find_all("a"):
        print(element.text)
        url2 = element.get("href")
        link_url = urllib.parse.urljoin(url,url2)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")