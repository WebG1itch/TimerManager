from tkinter import Toplevel, Label

class AdjustTimerWindow(Toplevel):
     
    def __init__(self, master):
         
        super().__init__()
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text ="This is a new Window")
        label.pack()