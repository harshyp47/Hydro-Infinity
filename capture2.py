import cv2
import time
cap =cv2.VideoCapture("D:\mark.mp4")
count = 1



while(True):

    ret, frame = cap.read()
    time.sleep(1)
    cv2.imwrite("D:\imagesdataset\Mark\img.png", frame)

    count =count+1

    cv2.imshow('Captured Frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
