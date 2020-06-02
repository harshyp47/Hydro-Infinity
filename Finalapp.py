import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter.ttk import *
import cv2
import pickle



def facerecog():

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

                #print("Access Granted!" + " Hello, " + str(name))


                return name



        cv2.imshow('Scanning...', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break






#------------------------------------------------------GUI SECTION -----------------------------------------------------------------------------------------------


class mclass:
    def __init__(self):
        self.window = window
        window.title("HYDRO - INFINITY WATER MONITOR")
        window.geometry("300x300")

        self.button1 = Button(window, text="analysis", command=self.plot)

        self.button1.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.button2 = Button(window, text="use water", command=self.scan)

        self.button2.place(relx=0.5, rely=0.6, anchor=CENTER)

    def plot(self):
        window.geometry("600x550")
        window.maxsize(600,550)
        self.button3 = Button(window, text="overuse data", command=self.mainmenu)
        self.button3.place(x=250,y=510)
        fig = Figure(figsize=(6, 5))
        a = fig.add_subplot(111)
        a.bar(x, v, color='red')
        a.set_title("Water Usage graph", fontsize=16)
        a.set_ylabel("Number of litres of water used", fontsize=10)
        a.set_xlabel("Name of water users", fontsize=10)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def scan(self):
        namevar = facerecog()
        if namevar:
            mclass.finish(self,name=namevar)



    def mainmenu(self):

        for i in range(len(usage)):
            if usage[i]>limit:
                print(person[i]+" has overused "+str(usage[i]-limit)+" Ltrs")


    def finish(self,name):
        window.geometry("600x350")
        window.maxsize(600,400)
        self.window = window
        fig = Figure(figsize=(6, 5))
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

        percentage = 100 - ( ((usagedict[name])/limit)*100)
        AccessGranted = Label(window, text="ACCESS GRANTED !").place(x=255, y=50)

        HelloUser = Label(window, text="Hello, {}".format(name)).place(x=270, y=80)

        Volume = Label(window, text="1.502 L").place(x=285, y=110)

        ConsumedAmount = Label(window, text="You have consumed  {} L  today !".format(usagedict[name])).place(x=215, y=170)

        HelloUser = Label(window, text="Remaining").place(x=30, y=250)

        Percentage = Label(window, text=str(percentage)+"%").place(x=525, y=250)

        pgbar = Progressbar(
            window,
            length=400,
            orient=HORIZONTAL,
            maximum=100,
            value=percentage,
            mode='determinate',
        )
        pgbar.pack()

        btn = tkinter.Button(
            window,
            text="Finish",
            command=exit,
        )
        pgbar.place(x=110, y=250)

        btn.place(x=280, y=280)


person =["lisa","mark"]
usagedict={"lisa":5,"mark":3.5}
usage=[5,3.5]
limit=2
x = np.array(person)
v = np.array(usage)
window = Tk()
start = mclass()
window.mainloop()
