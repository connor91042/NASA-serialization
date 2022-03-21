# Importing Libraries
import serial
import time

arduino = serial.Serial(port='COM19', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    input("Press enter:")
    send_string = "<L>"
    
    
    
    value = write_read(send_string)
    print(value) # printing the value
