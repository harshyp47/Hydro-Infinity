import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('D:\Cascades\haarcascade_frontalface_alt2.xml')
image_array=cv2.imread('D:\\imagesdataset\\Lisa\\lisa.jpg')

faces = face_cascade.detectMultiScale(image_array)
for (x, y, w, h) in faces:
    print("true")