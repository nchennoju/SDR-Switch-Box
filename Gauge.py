# !/usr/bin/env python3
import math
from tkinter import *
import tkinter as tk

#UNCOMMENT IF TESTING
#import time
#import random

class Gauge:

    def __init__(self, root, background):
        self.c = Canvas(root, width=190, height=150, bg=background, highlightthickness=0)
        self.xy = [(100.0, 90.0), (100.0, 40.0)]
        self.line = self.c.create_line(self.xy, width=5, fill='white')
        size = 180
        self.dark = self.c.create_arc(30, 20, size - 10, size - 10, style="arc", width=20, start=-10, extent=100,
                            outline="#8a1919", tags=('arc1', 'arc2'))
        #1f8749
        self.light = self.c.create_arc(30, 20, size - 10, size - 10, width=20, style="arc", start=90, extent=100,
                             outline="#ff0000", tags=('arc1', 'arc2'))
        #00ff65
        self.readout = self.c.create_text(100, 130, font=("Arial", int(size / 14), 'bold'), fill="white", text='')

    def setAngle(self, theta):
        radius = math.sqrt(pow(self.xy[1][0] - self.xy[0][0], 2) + pow(self.xy[1][1] - self.xy[0][1], 2))
        y = radius * math.sin(theta * math.pi / 180.0)
        x = radius * math.cos(theta * math.pi / 180.0)
        coor = [(100.0, 110.0)]
        if (theta < 0):
            coor.append([self.xy[0][0] - x, self.xy[0][1] - y])
        else:
            coor.append([self.xy[0][0] + x, self.xy[0][1] - y])
        self.c.coords(self.line, coor[0][0], coor[0][1], coor[1][0], coor[1][1])
        self.c.itemconfig(self.dark, start=-10, extent=theta + 10)
        self.c.itemconfig(self.light, start=theta, extent=190 - theta)

    def getWidget(self):
        return self.c

    def setText(self, str):
        self.c.itemconfig(self.readout, text=str)

win = tk.Tk()
win.title("Guage ELement")
win.geometry("800x200")
win.configure(bg='black')




#TEST CODE
'''g = Gauge(win, 'black')
g.getWidget().pack(side='bottom')


while True:
    angle = random.randint(-10, 190)
    g.setAngle(angle)
    time.sleep(0.1)
    win.update()

win.mainloop()'''