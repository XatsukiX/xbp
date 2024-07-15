import serial

arduino = serial.Serial('COM3', 9600) # COMポートは使用している環境に合わせて変更

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        print(data)