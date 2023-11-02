from bs4 import BeautifulSoup
import requests
from plyer import notification

def detect_updates():
    url = 'https://kulms.kanagawa-u.ac.jp/webclass/' #WebClassのURL
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser') #HTMLを解析
    
    elems=str(soup.select('course-contents-info')) 
   
   #strを使ってテキストに直している
    try:
        with open('old_elem.txt') as f: 
            old_elem = f.read()
    except:
        old_elem = ''
        #空の時を除いて開く
    if elems ==old_elem: #
        notification.notify(
    title="Webclass",
    message="課題はありません",
    app_name="Webclass",
    timeout=10
)
    #値が同じの時表示
    else:
        with open('old_elem.txt','w') as f: 
            f.write(elems)
            notification.notify(
    title="Webclass",
    message="締め切りの近い課題があります",
    app_name="Webclass",
    timeout=10
)
    #値が違う＝課題ができたときに表示
detect_updates()



