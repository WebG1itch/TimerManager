import tkinter as tk
from tkinter import TOP, ttk, LEFT

class TimerWidget(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.result_label = ttk.Label(self, text = "TESTEST")
        self.result_label.pack(side=LEFT, padx=5, pady=5)
