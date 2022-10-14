import tkinter as tk
from tkinter import TOP, ttk, LEFT
from tkinter.ttk import Button
from typing import Container

from Widgets.AdjustTimerWindow import AdjustTimerWindow


class ManagementBar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.AddTime = True

        AddTimerButton = Button(self, text="+ Add Timer", command = self.AddTimer)
        AddTimerButton.pack(side=LEFT, padx=5, pady=5)

        CountDownButton = Button(self, text="<", width = 4, command = self.CountDown)
        CountDownButton.pack(side=LEFT, padx=5, pady=2)

        CountUpButton = Button(self, text=">", width = 4, command = self.CountDown)
        CountUpButton.pack(side=LEFT, padx=5, pady=2)

        self.AdjustTimeButton = Button(self, text="⌛", width = 4, command = self.AdjustTime)
        self.AdjustTimeButton.pack(side=LEFT, padx=5, pady=2)


        ButtonTitles = {"30 Sec", "1 min", "3 min", "5 min", "10 min", "15 min", "30 min", "45 min", "1 hr"}
        self.ButtonList = []
        for title in ButtonTitles:
            AdjustTimeButton = Button(self, text=title, width = 6)
            AdjustTimeButton.pack(side=LEFT, padx=5, pady=2)
            self.ButtonList.append(AdjustTimeButton)

    def AddTimer(self):
        print("AddTimer called")

    def CountDown(self):
        print("CountDown")

    def CountUp(self):
        print("CountUp")

    def AdjustTime(self):
        AdjustTimerWindow(Container)