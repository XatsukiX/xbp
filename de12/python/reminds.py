import requests
from bs4 import BeautifulSoup
from plyer import notification
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

#関数を定義()
def d_confirm ():  
    #解析対象のURLを定義
    url= "https://kulms.kanagawa-u.ac.jp/webclass/"
    #URLの情報を取得
    res = requests.get(url)
    #
    soup = BeautifulSoup(res.text, "html.parser")
     #CSSセレクターで定義する asnはassignment=課題の略,
    asn = str(soup.select('course-contents-info'))

    #oasnが空の時をのぞいてoasnをテキストファイルとして保存
    try:
        with open('oasn.txt') as f: 
            oasn = f.read()
    except:
        oasn = ''

    #もしasnとoasnが同じ時デスクトップに表示
    if asn ==oasn: 
        notification.notify(
    title="Webclass",
    message="課題はありません",
    app_name="Webclass",
    timeout=10
)
    #それ以外＝課題があるときに表示
    else:
        with open('oasn.txt','w') as f: 
            f.write(asn)
            notification.notify(
    title="Webclass",
    message="締め切りの近い課題があります",
    app_name="Webclass",
    timeout=10
    )
            #サーバーに接続
            smtp_server = "smtp-mail.outlook.com"
            port = 587

            server = smtplib.SMTP(smtp_server, port)

            #暗号化の設定
            server.starttls()

            #サーバーにログイン
            login_address = "r202301989ko@jindai.jp"
            login_password = "u7LjzfbQmE"

            server.login(login_address, login_password)

            #メールの作成
            message = MIMEMultipart()

            message["Subject"] = "締め切りの近い課題があります。"
            message["From"] = "r202301989ko@jindai.jp"
            message["To"] = "r202301989ko@jindai.jp"

            text = MIMEText("締め切りの近い課題があります。")
            message.attach(text)

            #メールの送信
            server.send_message(message)
            #サーバーの切断
            server.quit()
            
#d_confirm関数を呼び出してデスクトップの表示とメールを送信（必要な時のみ）
d_confirm()