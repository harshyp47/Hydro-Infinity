import tkinter
from tkinter import *
from tkinter.ttk import *
import time

root = tkinter.Tk()
root.geometry("600x400")

limit = 2

AccessGranted = Label(root, text="ACCESS GRANTED !").place(x=255, y=50)

HelloUser = Label(root, text="Hello, User").place(x=270, y=80)

Volume = Label(root, text="1.502 L")

Volume.pack()
Volume.place(x=285, y=110)



ConsumedAmount = Label(root, text="You have consumed  3.5 L  today !")
ConsumedAmount.pack()
ConsumedAmount.place(x=215, y=170)

HelloUser = Label(root, text="Remaining").place(x=30, y=250)

Percentage = Label(root, text="")
Percentage.pack()
Percentage.place(x=525, y=250)

pgbar = Progressbar(
    root,
    length=400,
    orient=HORIZONTAL,
    maximum=100,
    value=20,
    mode='determinate',
)
pgbar.pack()

btn = tkinter.Button(
    root,
    text="Finish",
    command=exit,
)
pgbar.place(x=110, y=250)
btn.pack()
btn.place(x=280, y=280)
def change():
    Volume['text']=time.strftime("%H:%M:%S")
    Volume.after(200,change)
    percentage = 100 - (((5) / limit) * 100)
    Percentage['text']=str(percentage)+"%"
    pgbar['value']=percentage
    ConsumedAmount['text']="You have consumed  {} L  today !".format(5)

def exit():
    root.destroy()
change()
root.mainloop()



