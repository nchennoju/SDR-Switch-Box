# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
#import time
#import tkinter as tk

class Pipe:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        # DRAW PIPES
        if(fill):
            self.f0 = self.c.create_rectangle(7 * width / 16.0, 7 * height / 16.0, 9 * width / 16.0, 9 * height / 16.0,
                                                  fill=fluidColor)

        if (line_1):
            xy = [(7 * width / 16.0, 0), (7 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, 0), (9 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (7 * height / 16.0) + 1,
                                                  fill=fluidColor, outline="")
        else:
            xy = [(7 * width / 16.0, 7 * height / 16.0), (9 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
        if (line_2):
            xy = [(9 * width / 16.0, 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f2 = self.c.create_rectangle(9 * width / 16.0, (7 * height / 16.0) + 1, width,
                                                  (9 * height / 16.0) - 1,
                                                  fill=fluidColor, outline="")
        else:
            xy = [(9 * width / 16.0, 7 * height / 16.0), (9 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
        if (line_3):
            xy = [(7 * width / 16.0, 9 * height / 16.0), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, 9 * height / 16.0), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, 9 * height / 16.0, (9 * width / 16.0) - 1,
                                                  height,
                                                  fill=fluidColor, outline="")
        else:
            xy = [(7 * width / 16.0, 9 * height / 16.0), (9 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
        if (line_4):
            xy = [(0, 7 * height / 16.0), (7 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(0, 9 * height / 16.0), (7 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (7 * width / 16.0) + 1, (9 * height / 16.0) - 1,
                                                  fill=fluidColor, outline="")
        else:
            xy = [(7 * width / 16.0, 7 * height / 16.0), (7 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')



    def getWidget(self):
        return self.c


#TEST CODE
'''win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry("800x250")
win.configure(bg='black')

s = Pipe(win, 'black', 125, 125, True, True, False, True, '#41d94d', True)
s.getWidget().pack(side='bottom')

win.mainloop()'''