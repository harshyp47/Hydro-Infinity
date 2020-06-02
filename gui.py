import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter.ttk import *


class mclass:
    def __init__(self):
        self.window = window
        window.title("HYDRO - INFINITY WATER MONITOR")

        self.button1 = Button(window, text="analysis", command=self.plot)

        self.button1.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.button2 = Button(window, text="use water", command=self.scan)

        self.button2.place(relx=0.5, rely=0.6, anchor=CENTER)

    def plot(self):
        self.button3 = Button(window, text="overuse data", command=self.mainmenu)
        self.button3.place(relx=0.5, rely=0.75, anchor=CENTER)
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
        self.window = window
        fig = Figure(figsize=(6, 5))
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        self.button4 = Button(window, text="scanning", command=self.finish)
        self.button4.place(relx=0.5, rely=0.8, anchor=CENTER)

    def mainmenu(self):
        self.window = window
        self.button4 = Button(window, text="main menu", command=exit)
        self.button4.place(relx=0.5, rely=0.8, anchor=CENTER)

        details1 = Label(window, text=x[0] + " has overused ").place(relx=0.4, rely=0.83, anchor=CENTER)

        details2 = Label(window, text=(x[1] + " has overused ")).place(relx=0.4, rely=0.86, anchor=CENTER)
        details3 = Label(window, text=x[2] + " has overused ").place(relx=0.4, rely=0.89, anchor=CENTER)
        details4 = Label(window, text=x[3] + " has overused ").place(relx=0.4, rely=0.92, anchor=CENTER)

        details11 = Label(window, text=v[0]).place(relx=0.45, rely=0.83, anchor=CENTER)
        details21 = Label(window, text=v[1]).place(relx=0.45, rely=0.86, anchor=CENTER)
        details31 = Label(window, text=v[2]).place(relx=0.45, rely=0.89, anchor=CENTER)
        details41 = Label(window, text=v[3]).place(relx=0.45, rely=0.92, anchor=CENTER)
        details0 = Label(window, text="ltrs extra charge:").place(relx=0.49, rely=0.83, anchor=CENTER)
        details00 = Label(window, text="ltrs extra charge:").place(relx=0.49, rely=0.86, anchor=CENTER)
        details000 = Label(window, text="ltrs extra charge:").place(relx=0.49, rely=0.89, anchor=CENTER)
        details0000 = Label(window, text="ltrs extra charge:").place(relx=0.49, rely=0.92, anchor=CENTER)

    def finish(self):
        AccessGranted = Label(window, text="ACCESS GRANTED !").place(x=255, y=50)

        HelloUser = Label(window, text="Hello, User").place(x=270, y=80)

        Volume = Label(window, text="1.502 L").place(x=285, y=110)

        ConsumedAmount = Label(window, text="You have consumed  3.5 L  today !").place(x=215, y=170)

        HelloUser = Label(window, text="Remaining").place(x=30, y=250)

        Percentage = Label(window, text="20%").place(x=525, y=250)

        pgbar = Progressbar(
            window,
            length=400,
            orient=HORIZONTAL,
            maximum=100,
            value=20,
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


x = np.array(['Faisal', 'Harsh', 'Nidhi', 'Sristi', 'Ritav', 'sudha'])
v = np.array([10, 5, 6, 7, 3, 0])
window = Tk()
start = mclass()
window.mainloop()
