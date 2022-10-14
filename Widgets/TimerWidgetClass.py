# import the time module
import time
from unittest.util import _count_diff_all_purpose

"""

there are 6 funtions and they are as follows

countdown
countup
subtime(amount)
addtime(amout)
pause
play

"""


#varibles
inputTime = input("Enter the time in seconds: ")
inputTime = int(inputTime)
amount = 0
pauseMoment = False
subTimeMoment = False
addTimeMoment = False
playMoment = False


# funtions
def tick(): # this one doesnt work /is wip kinda i dont feel like finishing it
    global amount
    cantick = True
    while cantick == True:
        if subTime == True:
            inputTime -= amount
        
def countdown():
    global inputTime
    global pauseMoment
    global amount
    running = True
    startTime = time.time()
    zero = 0
    while running == True:
        deltaTime = time.time() - startTime
        deltaTime = int(deltaTime)
        deltaInputTime = inputTime - deltaTime
        if deltaTime != zero:
            zero = deltaTime
            print(inputTime - deltaTime)
        if deltaInputTime <= 0:
            running = False
    # main add/sub/play/pause logic checks evertime the while loop goes
    if pauseMoment == True:
        running = False
    if playMoment == True:
        running = True
    if amount != 0 and subTimeMoment == True:
        inputTime -= amount
        amount = 0
    elif addTimeMoment == True:
        inputTime += amount
        amount = 0

def countUp():
    global inputTime
    global amount
    global addTimeMoment
    global subTimeMoment
    running = True
    startTime = time.time()
    zero = 0
    while running == True:
        deltaTime = time.time() - startTime
        deltaTime = int(deltaTime)
        if deltaTime != zero:
            zero = deltaTime
            print(deltaTime)
        if deltaTime > (inputTime - 1):
            running = False
    # main add/sub/play/pause logic checks evertime the while loop goes
    if pauseMoment == True:
        running = False
    if playMoment == True:
        running = True
    if amount != 0 and subTimeMoment == True:
        inputTime -= amount
        amount = 0
    elif addTimeMoment == True:
        inputTime += amount
        amount = 0

def subTime(x):
    global amount
    global subTimeMoment
    subTimeMoment = True
    amount = x

def addTime(x):
    global amount
    global addTimeMoment
    addTimeMoment = True
    amount = x

def pause():
    global pauseMoment
    pauseMoment = False

def play():
    global playMoment
    playMoment = True

# function call
countdown()