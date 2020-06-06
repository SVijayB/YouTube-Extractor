from tkinter import *
from Modules.SelectionWindow import SelectionWindow

if __name__ == "__main__":
    window = Tk()
    window.state("zoomed")
    data = open("../version.txt" , "r").read()
    print("YouTube Extractor | " + data)
    window.title("YouTube Extractor | " + data)
    window.iconbitmap("../assets/favicon_io/favicon.ico")
    app = SelectionWindow(window)
    window.mainloop()