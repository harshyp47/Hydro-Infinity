import cv2
import pickle


face_cascade = cv2.CascadeClassifier('D:\Cascades\haarcascade_frontalface_alt2.xml')



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")

labels = {}
with open("face-labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

frame = cv2.imread("D:\imagesdataset\Mark\mark.jpg")
#frame = cv2.imread("D:\imagesdataset\Lisa\lisa.jpg")
#cap = cv2.VideoCapture("D:\mark.mp4")

person =["lisa","mark"]

while(True):

    #ret, frame = cap.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]


        id_, conf = recognizer.predict(roi_gray)
        if conf>=4 and conf <= 85:

            name = labels[id_]
            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (0, 255, 0)
            stroke = 1
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)


            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

            print("Access Granted!" + " Hello, " + str(name))



    cv2.imshow('Scanning...', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break






