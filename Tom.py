
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("866x654")
image=Image.open("appstore.png")
photo=ImageTk.PhotoImage(image)
L=Label(image=photo)
L.pack()
root.mainloop()