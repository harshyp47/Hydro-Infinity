from tkinter import *
import imageio
from PIL import Image, ImageTk
def stream():
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return
########### Main Program ############
root = Tk()
root.title('Video in a Frame')
f1=Frame()
l1 = Label(f1)
l1.pack()
f1.pack()
video_name = "D:\mark.mp4"   #Image-path
video = imageio.get_reader(video_name)
delay = int(1000 / video.get_meta_data()['fps'])
stream()
root.mainloop()