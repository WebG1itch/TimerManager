from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
from Widgets.ManagementBarClass import ManagementBar
from Widgets.TimerWidgetClass import TimerWidget

class Timer(Tk):
    def __init__(self):
        super().__init__()

        self.title('Timer 2.0')
        self.geometry("1350x750")
        self.initUI()

    def initUI(self):
        ManagementBarFrame = ManagementBar(self)
        ManagementBarFrame.pack(fill=X)
        lbl1 = Label(ManagementBarFrame, text="Title", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(ManagementBarFrame)
        entry1.pack(fill=X, padx=5, expand=True)

        frame3 = TimerWidget(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

if __name__ == "__main__":
    app = Timer()
    app.mainloop()