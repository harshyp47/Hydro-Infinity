import tkinter 
from tkinter import *
from tkinter.ttk import *

root = tkinter.Tk()
root.geometry("600x400")

AccessGranted = Label(root, text = "ACCESS GRANTED !").place(x = 255,y = 50)  
  
HelloUser = Label(root, text = "Hello, User").place(x = 270, y = 80)

Volume = Label(root, text = "1.502 L").place(x = 285, y = 110)

ConsumedAmount = Label(root, text = "You have consumed  3.5 L  today !").place(x = 215, y = 170)

HelloUser = Label(root, text = "Remaining").place(x = 30, y = 250)

Percentage = Label(root, text = "20%").place(x = 525, y = 250)

pgbar = Progressbar(
    root,
    length = 400,
    orient = HORIZONTAL,
    maximum = 100,
    value = 20,
    mode='determinate',
)
pgbar.pack()

btn = tkinter.Button(
    root,
    text = "Finish",
    command = exit,
)
pgbar.place(x = 110, y = 250)
btn.pack()
btn.place(x = 280, y = 280)  
root.mainloop()

def exit():
    root.destroy()
