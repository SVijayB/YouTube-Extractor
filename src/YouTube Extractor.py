from pytube import YouTube
from tkinter import *
import re
import threading

class application():
    def __init__(self,root):
        self.root = root
        self.root.grid_rowconfigure(0,weight=2)
        self.root.grid_columnconfigure(0,weight=1)
        self.root.configure(bg="black")
        self.heading = Label(self.root,text = "YOUTUBE EXTRACTOR",fg = "green",
        bg = "black", font=("Castellar", 70))
        self.heading.grid(pady = (0,10))
        self.link = Label(self.root,text="Paste the YouTube Link Below", 
        fg = "white", bg = "black", font=("Algerian", 30))
        self.link.grid(pady = (0,20))
        self.entryvar = StringVar()
        self.entry = Entry(self.root, width= 70, textvariable = self.entryvar, 
        fg = "green", bg="white", font=("Agency Fb",25))
        self.entry.grid(pady = (0,15), ipady=2)
        self.error = Label(self.root, text="", font=("Concert One",20))
        self.error.grid(pady=(0,8))
        self.save = Label(self.root,text="Select The Location You Want To Save In", 
        fg = "white",bg = "black", font=("Algerian",30))
        self.save.grid()
        self.directory = Button(self.root, text="Location",
        fg = "white", bg = "black",font = ("Bell MT", 15),command = self.openDirectory)
        self.directory.grid(pady=(10,3))

if __name__ == "__main__":
    window = Tk()
    window.state("zoomed")
    app = application(window)
    window.mainloop()