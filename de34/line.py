import requests

LINE_NOTIFY_TOKEN = 'YOUR_ACCESS_TOKEN'
LINE_NOTIFY_API = 'https://notify-api.line.me/api/notify'

def send_line_message(message):
    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }
    data = {
        'message': message
    }
    requests.post(LINE_NOTIFY_API, headers=headers, data=data)

import serial

arduino = serial.Serial('COM3', 9600) # COMポートは使用している環境に合わせて変更

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        print(data)
        send_line_message(data)
