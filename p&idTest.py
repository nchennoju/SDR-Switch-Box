# !/usr/bin/env python3
from tkinter import *

# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

#UNCOMMENT IF TESTING
import time
from random import randint
import tkinter as tk

import Nozzle
import Tank
import Valves
import Pipes

width = 600
height = 1000

win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry(str(width) + "x" + str(height))
win.configure(bg='black')

win_w = width
win_h = height


ln1 = Pipes.Vertical(win, 'black', win_w*(125.0/600), win_h*0.17)
ln1.getWidget().place(x=win_w * 0.05, y=win_h * 0.1)
ln2 = Pipes.Vertical(win, 'black', win_w*(125.0/600), win_h*0.08)
ln2.getWidget().place(x=win_w * 0.55, y=win_h * 0.27)
ln3 = Pipes.Vertical(win, 'black', win_w*(125.0/600), win_h*0.08)
ln3.getWidget().place(x=win_w * 0.05, y=win_h * 0.27)
ln4 = Pipes.Vertical(win, 'black', win_w*(125.0/600), win_h*0.45)
ln4.getWidget().place(x=win_w * 0.25, y=win_h * 0.1)
ln5 = Pipes.Vertical(win, 'black', win_w*(125.0/600), win_h*0.15)
ln5.getWidget().place(x=win_w * 0.05, y=win_h * 0.35)
ln6 = Pipes.Vertical(win, 'black', win_w*(125.0/600), win_h*0.15)
ln6.getWidget().place(x=win_w * 0.55, y=win_h * 0.35)
ln7 = Pipes.Horizontal(win, 'black', win_w*(125.0/600), win_h*0.15)
ln7.getWidget().place(x=win_w * 0.36, y=win_h * 0.22)




he = Tank.Tank(win, 'black', 'He', '#1d2396', win_w*(125.0/600), 125)
he.getWidget().place(x=win_w * 0.05, y=win_h * 0.1)
gn2 = Tank.Tank(win, 'black', 'GN2', '#1d2396', win_w*(125.0/600), 125)
gn2.getWidget().place(x=win_w * 0.25, y=win_h * 0.1)
s = Valves.Solenoid(win, 'black', 1, win_w*(125.0/600), 50, True, False, True, False)
s.getWidget().place(x=win_w * 0.05, y=win_h * 0.27)
lox = Tank.Tank(win, 'black', 'LOx', '#1d2396', win_w*(125.0/600), 125)
lox.getWidget().place(x=win_w * 0.05, y=win_h * 0.35)
st = Valves.Stepper(win, 'black', win_w*(125.0/600), 50, True, False, True, False)
st.getWidget().place(x=win_w * 0.05, y=win_h * 0.5)
s2 = Valves.Solenoid(win, 'black', 1, win_w*(125.0/600), 50, False, False, True, True)
s2.getWidget().place(x=win_w * 0.55, y=win_h * 0.27)
k = Tank.Tank(win, 'black', 'K', '#1d2396', win_w*(125.0/600), 125)
k.getWidget().place(x=win_w * 0.55, y=win_h * 0.35)
st2 = Valves.Stepper(win, 'black', win_w*(125.0/600), 50, True, False, True, False)
st2.getWidget().place(x=win_w * 0.55, y=win_h * 0.5)
s3 = Valves.Solenoid(win, 'black', 1, win_w*(125.0/600), 50, False, True, False, True)
s3.getWidget().place(x=win_w * 0.15, y=win_h * 0.55)
s4 = Valves.Solenoid(win, 'black', 1, win_w*(125.0/600), 50, False, True, False, True)
s4.getWidget().place(x=win_w * 0.35, y=win_h * 0.55)
n = Nozzle.Nozzle(win, 'black', win_w/6.0, 150)
n.getWidget().place(x=win_w * 0.35, y=win_h * 0.8)


ln8 = Pipes.Vertical(win, 'black', win_w*(25.0/600), win_h*0.074)
ln8.getWidget().place(x=win_w * 0.3325, y=win_h * 0.5)
ln9 = Pipes.Vertical(win, 'black', win_w*(25.0/600), win_h*0.074)
ln9.getWidget().place(x=win_w * 0.3325, y=win_h * 0.5)


while True:
    win_h = win.winfo_height()
    win_w = win.winfo_width()

    ret, frame = vid.read()
    '''cv2.resizeWindow('frame', 1400, 450)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)'''

    # Display the resulting frame
    cv2.imshow('frame', frame)
    #print(str(win_w) + " " + str(win_h))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i = randint(0, 100)
    b = randint(0, 1)
    he.setTankLevel(i)
    he.setTankReadout(i, i)
    gn2.setTankLevel(i)
    gn2.setTankReadout(i, i)
    lox.setTankLevel(i)
    lox.setTankReadout(i, i)
    k.setTankLevel(i)
    k.setTankReadout(i, i)
    n.setNozzleReadout(i, i)
    st.setPercentage(i)
    st2.setPercentage(i)
    win.update()
    s.setState(b)
    s2.setState(b)
    s3.setState(b)
    s4.setState(b)
    s.setState(b)
    s2.setState(b)
    s3.setState(b)
    s4.setState(b)
    #time.sleep(0.01)

#win.mainloop()

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()