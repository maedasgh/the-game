from tkinter import *
class s():
    w = Tk()
    canvas=Canvas(w, width = 800, height = 800)
    canvas.pack()
    i=PhotoImage (file='C:\\Users\\PDA-pc01\\Desktop\\background.gif')
    canvas.create_image(0, 0, anchor =NW, image=i)


