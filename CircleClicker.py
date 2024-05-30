#   ____ _          _         ____                     _                __  __            _     _
#  / ___(_)_ __ ___| | ___   |  _ \ _ __ __ ___      _(_)_ __   __ _   |  \/  | __ _  ___| |__ (_)_ __   ___
# | |   | | '__/ __| |/ _ \  | | | | '__/ _` \ \ /\ / / | '_ \ / _` |  | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
# | |___| | | | (__| |  __/  | |_| | | | (_| |\ V  V /| | | | | (_| |  | |  | | (_| | (__| | | | | | | |  __/
#  \____|_|_|  \___|_|\___|  |____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |  |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
#                                                              |___/ 
# By Sam Rohrbach (github.com/TesseractPi)
# Built for Neal.fun's perfect circle test at https://neal.fun/perfect-circle/
# This should be on my website (https://samrohrbach.space)
# In its default state, this is built for a 1366x768 screen in fullscreen. Change the values accordingly. 

import time # just casually bringing in the tardis
import tkinter as tk # to get screen width and height
import win10toast # to send notifications
import pyautogui # so we can click the mouse
import keyboard # to detect keypresses
import math # to do some circle stuff

### Win10Toast Setup ###
toast = win10toast.ToastNotifier() # set up win10toast

### Screen width stuff ###
root = tk.Tk() # set up tkinter
screen_width = root.winfo_screenwidth() # get screen width
screen_height = root.winfo_screenheight() # get screen height

center_x = (screen_width / 2) + 0.5 # center x of circle
center_y = 364.5 # center y of circle
radius = 256 # radius of circle

angle_increment = 6 # must be divisible by 360 AND be less than 180, THIS IS THE VARIABLE YOU SHOULD CHANGE!
angle_repeat = int((360 / angle_increment) + 1) # how many times to repeat moving the mouse
angle = 0 # starting angle, DO NOT CHANGE THIS!

def notify(title, bottomtext):
    toast.show_toast(
    title,
    bottomtext,
    #duration = 0,
    #threaded = True,
    )

def getXY(thetaThing):
    x = (radius * math.sin(math.pi * 2 * angle / 360)) + center_x
    y = (radius * math.cos(math.pi * 2 * angle / 360)) + center_y
    return (x, y)

print("Press A to draw a circle, or press Q to quit")

while True:
    if keyboard.is_pressed('q'):
        print("Goodbye!")
        notify("Exiting...", "Goodbye!")
        break
    
    if keyboard.is_pressed('a'):
        pyautogui.moveTo(center_x, (center_y + radius))
        time.sleep(0.25)
        pyautogui.mouseDown() # start holding the mouse down
        print("Circle started... ") # just to add some flair
        for i in range(angle_repeat):
            pyautogui.moveTo(getXY(angle))
            print(getXY(angle)) # for debugging purposes and to look cool
            angle = angle + angle_increment # just add a little to the circle each time
        pyautogui.mouseUp() # release the mouse
        print("Circle finished! Press A to draw another circle or Q to quit") # you won't be looking at this anyway
        notify("Circle finished!", "Press A to draw another circle or press Q to quit.") # you'll be looking at this
        #break
# this line is here to be 69 lines long and the last char here is 69