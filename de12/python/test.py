import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

url="https://api.openweathermap.org/data/2.5/forecast?q={city}&appid{key}&lang=ja&units=metric"
url= url.format(city="Yokohama,JP",key="8244421fd46689f818a49b723dca75c9")

jsondata = requests.get(url).json()
df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9), "JST")
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"],tz))[:-9]
    temp = dat["main"]["temp"]
    df.loc[jst] = temp

df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()
plt.show()