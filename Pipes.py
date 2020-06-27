# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
#import time
#import tkinter as tk

class Vertical:
    def __init__(self, root, background, width, height):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.line = self.c.create_line(width/2.0, 0, width/2.0, height, width=3, fill='white')

    def getWidget(self):
        return self.c

    def setState(self, open):
        if(open):
            self.c.itemconfig(self.line, fill='#41d94d')
        else:
            self.c.itemconfig(self.line, fill = '#ab1f1f')

class Horizontal:
    def __init__(self, root, background, width, height):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.line = self.c.create_line(0, height/2.0, width, height/2.0, width=3, fill='white')

    def getWidget(self):
        return self.c

    def setState(self, open):
        if (open):
            self.c.itemconfig(self.line, fill='#41d94d')
        else:
            self.c.itemconfig(self.line, fill='#ab1f1f')

class Elbow:
    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        if(line_1):
            self.line = self.c.create_line(width/2.0, height/2.0, width/2.0, 0)
            self.line2 = self.c.create_line(width / 2.0, height / 2.0, width, height/2.0)
        if(line_2):
            self.line = self.c.create_line(width / 2.0, height / 2.0, width, height/2.0)
            self.line2 = self.c.create_line(width / 2.0, height / 2.0, width/2.0, height)
        if(line_3):
            self.line = self.c.create_line(width / 2.0, height / 2.0, width / 2.0, height)
            self.line2 = self.c.create_line(width / 2.0, height / 2.0, 0, height/2.0)
        if(line_4):
            self.line = self.c.create_line(width / 2.0, height / 2.0, 0, height/2.0)
            self.line2 = self.c.create_line(width / 2.0, height / 2.0, width/2.0, 0)


    def getWidget(self):
        return self.c

    def setState(self, open):
        if (open):
            self.c.itemconfig(self.line, fill='#41d94d')
            self.c.itemconfig(self.line2, fill='#41d94d')
        else:
            self.c.itemconfig(self.line, fill='#ab1f1f')
            self.c.itemconfig(self.line2, fill='#ab1f1f')