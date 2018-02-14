import tkinter as tk                
from tkinter import font  as tkfont 
from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import Button
import tkinter.messagebox
from grid import App
import requests

session = requests.session()

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.curFrame = None
        
        self.frames = {}
        for F in (Pageshoro, Play, Twoplayer, Fourplayer, PageRegister, PageLogin,Rank):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Pageshoro")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        if self.curFrame != None:
            self.curFrame.destroy()
            
        curFrame = self.frames[page_name]
        curFrame.tkraise()


class Pageshoro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        label = tk.Label(self, text="Main menu",bg='black',fg='white', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Play", bg='black',fg='white',width=23,
                            command=lambda: controller.show_frame("Play"))
        button2 = tk.Button(self, text="Register", bg='black',fg='white',width=23,
                            command=lambda: controller.show_frame("PageRegister"))
        button3 = tk.Button(self, text="Login", bg='black',fg='white',width=23,
                            command=lambda: controller.show_frame("PageLogin"))
        button4 = tk.Button(self, text="Logout", bg='black',fg='white',width=23,
                            command=self.Logout)
        button5 = tk.Button(self, text="Scores", bg='black',fg='white',width=23,
                            command=lambda: controller.show_frame("Rank"))
        button6 = tk.Button(self, text="Quit", bg='black',fg='white',width=23,
                            command=self.quit)
        
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
    def quit(self):
        self.controller.destroy()
    def Logout(self):
        request = session.post('http://127.0.0.1:5000/Logout')
        

#play page
class Play(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        label = tk.Label(self, text="choose number of players:",bg='black',fg='white', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Quoridor 2 player",bg='black',fg='white',width=23,
                           command=lambda: controller.show_frame("Twoplayer"))
        button2 = tk.Button(self, text="Quoridor 4 player",bg='black',fg='white',width=23,
                           command=lambda: controller.show_frame("Fourplayer"))
        button3 = tk.Button(self, text="Back",bg='black',fg='white',width=23,
                           command=lambda: controller.show_frame("Pageshoro"))
        button1.pack()
        button2.pack()
        button3.pack()





#2player page
class Twoplayer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="black")
        self.controller = controller
        self.buttons = [[""] * 9] * 9
        self.lines = [[""] * 8] * 9
        self.walls = [[""]*9]*8
        for i in range(1, 10):
            for j in range(1, 10):
                self.buttons[i - 1][j - 1] = tk.Button(self, bg="lightyellow")
                self.buttons[i - 1][j - 1].place(relx=i * 0.09, rely=j * 0.09, height=40, width=40)

        for i in range(1, 10):
            for j in range(1, 9):
                self.lines[i-1][j-1] = tk.Button(self, bg="yellow")
                self.lines[i - 1][j - 1].place(relx=i * 0.09, rely=(j+0.75) * 0.09, height=10, width=40)

        for i in range(1, 9):
            for j in range(1, 10):
                self.walls[i-1][j-1] = tk.Button(self, bg="green")
                self.walls[i - 1][j - 1].place(relx=(i+0.75) * 0.09, rely=j * 0.09, height=40, width=10)
                
        button3 = tk.Button(self, text="Back",bg='black',fg='white',width=10,
                           command=lambda: controller.show_frame("Play"))
        button3.pack(side="bottom")


       

    def movement():
        pass

        
        
    def server1():
        pass
        
        

class Fourplayer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="black")
        self.controller = controller
        self.buttons = [[""] * 9] * 9
        self.lines = [[""] * 8] * 9
        self.walls = [[""]*9]*8
        for i in range(1, 10):
            for j in range(1, 10):
                self.buttons[i - 1][j - 1] = tk.Button(self, bg="lightgreen")
                self.buttons[i - 1][j - 1].place(relx=i * 0.09, rely=j * 0.09, height=40, width=40)

        for i in range(1, 10):
            for j in range(1, 9):
                self.lines[i-1][j-1] = tk.Button(self, bg="lightyellow")
                self.lines[i - 1][j - 1].place(relx=i * 0.09, rely=(j+0.75) * 0.09, height=10, width=40)

        for i in range(1, 9):
            for j in range(1, 10):
                self.walls[i-1][j-1] = tk.Button(self, bg="grey")
                self.walls[i - 1][j - 1].place(relx=(i+0.75) * 0.09, rely=j * 0.09, height=40, width=10)
                
        button3 = tk.Button(self, text="Back",bg='black',fg='white',width=10,
                           command=lambda: controller.show_frame("Play"))
        button3.pack(side="bottom")

    def server2():
        pass
        
               

        
#Register page
class PageRegister(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        label = tk.Label(self, text="Register",bg='black',fg='white', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label2 = tk.Label(self, text="Name:", bg="black", fg="white", font="none 10 bold" )
        Label2.pack()
        self.entName=Entry(self)
        self.entName.pack()
        Label3=tk.Label(self, text="Username:", bg="black", fg="white", font="none 10 bold" )
        Label3.pack()
        self.entUername=Entry(self)
        self.entUername.pack()
        Label4=tk.Label(self, text="Password:", bg="black", fg="white", font="none 10 bold" )
        Label4.pack()        
        self.entPassword=Entry(self)
        self.entPassword.pack()
        Label5=tk.Label(self, text="Confrim Password:", bg="black", fg="white", font="none 10 bold" )
        Label5.pack()        
        self.entCPassword=Entry(self)
        self.entCPassword.pack()
        Label2 = tk.Label(self, text="",bg="black")
        Label2.pack()
        self.khoroji= Text(self,width=15,height=1,wrap=WORD,background="gray")
        self.khoroji.pack()
        
        button = tk.Button(self, text="Get register",bg='black',fg='yellow',width=23,
                           command= self.server4)
        button3 = tk.Button(self, text="Back",bg='black',fg='white',width=23,
                           command=lambda: controller.show_frame("Pageshoro"))
        button.pack()
        button3.pack()

    def server4(self):
        if(self.entPassword.get() != self.entCPassword.get()):
            self.khoroji.insert(END, "Wrong!!!")
        if(self.entPassword.get()==""):
            self.khoroji.insert(END, "Wrong!!!")
        if(self.entCPassword.get()==""):
            self.khoroji.insert(END, "Wrong!!!")
        if(self.entName.get()==""):
            self.khoroji.insert(END, "Wrong!!!")
        if(self.entUername.get()==""):
            self.khoroji.insert(END, "Wrong!!!")
        else:
            self.khoroji.delete(0.0, END)
            request = session.post('http://127.0.0.1:5000/Register', data={'username': self.entUername.get(), 'password': self.entPassword.get()})
            if(request.text == "successful"):
                self.controller.show_frame("PageLogin")
            else:
                self.khoroji.insert(END, request.text)
        
#loginpage        
class PageLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Login:", bg="black", fg="white",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label3=tk.Label(self, text="Username:", bg="black", fg="white", font="none 10 bold" )
        Label3.pack()
        self.entN=Entry(self)
        self.entN.pack()
        Label4=tk.Label(self, text="Password:", bg="black", fg="white", font="none 10 bold" )
        Label4.pack()        
        self.entP=Entry(self)
        self.entP.pack()
        button = tk.Button(self, text="Get Login", bg="black", fg="green",
                           command= self.server5)
        button3 = tk.Button(self, text="Back",bg='black',fg='white',width=23,
                           command=lambda: controller.show_frame("Pageshoro"))
        Label2 = tk.Label(self, text="",bg="black")
        Label2.pack()
        self.khoroji= Text(self,width=55,height=1,wrap=WORD,background="gray")
        self.khoroji.pack()
        
        button.pack()
        button3.pack()

    def server5(self):
        self.khoroji.delete(0.0, END)
        if(self.entN.get()==""):
            self.khoroji.insert(END, "Wrong!!!")
        if(self.entP.get()==""):
            self.khoroji.insert(END, "Wrong!!!")
        else:
            request = session.post('http://127.0.0.1:5000/Login', data={'username': self.entN.get(), 'password': self.entP.get()})
            if(request.text == "successful"):
                self.controller.show_frame("Play")
            else:
                self.khoroji.insert(END, request.text)
#page Rank
class Rank(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        self.khoroji= Text(self,width=90,height=50,wrap=WORD,background="gray")
        self.khoroji.pack()
        button3 = tk.Button(self, text="Back",bg='black',fg='white',width=100,
                           command=lambda: controller.show_frame("Pageshoro"))
        button3.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
