import serial
import cv2
import  matplotlib


arduino = serial.Serial('COM3', 38400, timeout=.1)
while True:
    data = arduino.readline()  # the last bit gets rid of the new-line chars
    if data:
        print(data.decode('utf-8'))
