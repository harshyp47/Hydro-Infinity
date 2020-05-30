import cv2
import time
cap =cv2.VideoCapture("D:\mark.mp4")
count = 1

name= "Mark"

while(True):

    ret, frame = cap.read()
    time.sleep(1)
    cv2.imwrite("D:\imagesdataset\{}\img{}.png".format(name, count), frame)

    count =count+1

