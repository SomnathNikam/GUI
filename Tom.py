
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
image=Image.open("giri.jpeg")
photo=ImageTk.PhotoImage(image)
L=Label(image=photo)
L.pack()
root.mainloop()