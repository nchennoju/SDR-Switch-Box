# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
#import time
#import tkinter as tk

class Solenoid:

    def __init__(self, root, background, num, width, height, line_1, line_2, line_3, line_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.fill = self.c.create_rectangle((width/4.0), (height/4.0), (width*(3/4.0)), (height*(3/4.0)), fill='#ab1f1f')
        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')

        xy = []
        if(line_1):
            xy = [(width/2.0, height/4.0), (width/2.0, 0)]
            self.c.create_line(xy, width=3, fill='white')
        if(line_2):
            xy = [(width*(3/4.0), height/2.0), (width, height/2.0)]
            self.c.create_line(xy, width=3, fill='white')
        if(line_3):
            xy = [(width/2.0, height*(3/4.0)), (width/2, height)]
            self.c.create_line(xy, width=3, fill='white')
        if(line_4):
            xy = [(width/4.0, height/2.0), (0, height/2.0)]
            self.c.create_line(xy, width=3, fill='white')

        self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 10, 'bold'), fill="white", text=str(num))

    def getWidget(self):
        return self.c

    def setState(self, open):
        if(open):
            self.c.itemconfig(self.fill, fill='#41d94d')
        else:
            self.c.itemconfig(self.fill, fill = '#ab1f1f')


class Stepper:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4):
        padding = 25

        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.fill = self.c.create_rectangle((width/4.0), (height/4.0), (width*(3/4.0)), (height*(3/4.0)), fill='#ab1f1f')
        self.fillGreen = self.c.create_rectangle((width / 4.0), (height / 4.0), (width / 4.0), (height * (3 / 4.0)), fill='#41d94d')
        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')

        xy = []
        if(line_1):
            xy = [(width/2.0, height/4.0), (width/2.0, 0)]
            self.c.create_line(xy, width=3, fill='white')
        if(line_2):
            xy = [(width*(3/4.0), height/2.0), (width, height/2.0)]
            self.c.create_line(xy, width=3, fill='white')
        if(line_3):
            xy = [(width/2.0, height*(3/4.0)), (width/2, height)]
            self.c.create_line(xy, width=3, fill='white')
        if(line_4):
            xy = [(width/4.0, height/2.0), (0, height/2.0)]
            self.c.create_line(xy, width=3, fill='white')

        self.percentage = self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 10, 'bold'), fill="white", text="Percentage")

    def getWidget(self):
        return self.c

    def setPercentage(self, p):
        self.c.itemconfig(self.percentage, text=str(p)+' %')
        self.c.coords(self.fillGreen, (self.width / 4.0), (self.height / 4.0), (self.width / 4.0) + ((p/100.0)*self.width/2.0), (self.height * (3 / 4.0)))

#TEST CODE
'''win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry("800x200")
win.configure(bg='black')

s = Solenoid(win, 'black', 1, 100, 50, True, True, True, True)
s.getWidget().pack(side='bottom')
st = Stepper(win, 'black', 100, 50, False, False, False, False)
st.getWidget().pack(side='top')

while True:
    s.setState(True)
    win.update()
    time.sleep(1)
    s.setState(False)
    win.update()
    time.sleep(1)
    for i in range(101):
        st.setPercentage(i)
        time.sleep(0.01)
        win.update()


win.mainloop()'''