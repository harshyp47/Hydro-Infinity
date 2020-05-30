from tkinter import *
from PIL import ImageTk,Image
import cv2
root = Tk()
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()

cap = cv2.VideoCapture("D:\mark.mp4")

while(True):

    ret,frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(img)
    tikimg = ImageTk.PhotoImage(pilimg)
    canvas.create_image(150, 40, anchor=NW, image=tikimg)
    root.mainloop()
