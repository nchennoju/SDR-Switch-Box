# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
#import time
#import tkinter as tk

class Solenoid:

    def __init__(self, root, background, num, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.fill = self.c.create_rectangle((width/4.0), (height/4.0), (width*(3/4.0)), (height*(3/4.0)), fill='#ab1f1f')
        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')

        #DRAW PIPES
        if(line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        #DRAW FLOW
        if(fill_1):
            self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                                fill=fluidColor, outline="")
        if(fill_2):
            self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width, (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")
        if(fill_3):
            self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1, height,
                                              fill=fluidColor, outline="")
        if(fill_4):
            self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")

        self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 10, 'bold'), fill="white", text=str(num))

    def getWidget(self):
        return self.c

    def setState(self, open):
        if(open):
            self.c.itemconfig(self.fill, fill='#41d94d')
        else:
            self.c.itemconfig(self.fill, fill = '#ab1f1f')


class Stepper:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.fill = self.c.create_rectangle((width/4.0), (height/4.0), (width*(3/4.0)), (height*(3/4.0)), fill='#ab1f1f')
        self.fillGreen = self.c.create_rectangle((width / 4.0), (height / 4.0), (width / 4.0), (height * (3 / 4.0)), fill='#41d94d')
        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')

        # DRAW PIPES
        if (line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if (line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if (line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if (line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        # DRAW FLOW
        if (fill_1):
            self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                              fill=fluidColor, outline="")
        if (fill_2):
            self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width,
                                              (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")
        if (fill_3):
            self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1,
                                              height,
                                              fill=fluidColor, outline="")
        if (fill_4):
            self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")

        self.percentage = self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 10, 'bold'), fill="white", text="_ _ %")

    def getWidget(self):
        return self.c

    def setPercentage(self, p):
        self.c.itemconfig(self.percentage, text=str(p)+' %')
        self.c.coords(self.fillGreen, (self.width / 4.0), (self.height / 4.0), (self.width / 4.0) + ((p/100.0)*self.width/2.0), (self.height * (3 / 4.0)))

class Orifice:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')
        self.c.create_line((width / 4.0, height / 2.0), (3 * width / 4.0, height / 2.0), width=1, fill='white')
        self.beforeP = self.c.create_text(width / 2.0, 3 * height / 8.0, font=("Arial", 8, 'bold'), fill="white",
                                             text="B: __ Pa")
        self.afterP = self.c.create_text(width / 2.0, 5 * height / 8.0, font=("Arial", 8, 'bold'), fill="white",
                                         text="A: __ Pa")
        self.name = self.c.create_text(width/4.0, height/8.0, font=("Arial", 6, 'bold'), fill="white",
                                         text="Orifice")

        #DRAW PIPES
        if(line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        #DRAW FLOW
        if(fill_1):
            self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                                fill=fluidColor, outline="")
        if(fill_2):
            self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width, (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")
        if(fill_3):
            self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1, height,
                                              fill=fluidColor, outline="")
        if(fill_4):
            self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")


    def getWidget(self):
        return self.c

    def setValues(self, before, after):
        self.c.itemconfig(self.beforeP, text='B: ' + before + ' Pa')
        self.c.itemconfig(self.afterP, text='A: ' + after + ' Pa')

class PressureSensor:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.rect = self.c.create_oval(width / 4.0, height / 4.0, width * (3 / 4.0), height * (3 / 4.0),
                                            outline='white', width=1)
        self.p = self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 10, 'bold'), fill="white",
                                             text="__ Pa")
        self.name = self.c.create_text(width/4.0, height/8.0, font=("Arial", 6, 'bold'), fill="white",
                                         text="Pressure\nSensor")

        #DRAW PIPES
        if(line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        #DRAW FLOW
        if(fill_1):
            self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                                fill=fluidColor, outline="")
        if(fill_2):
            self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width, (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")
        if(fill_3):
            self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1, height,
                                              fill=fluidColor, outline="")
        if(fill_4):
            self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                              fill=fluidColor, outline="")

    def getWidget(self):
        return self.c

    def setValues(self, pressure):
        self.c.itemconfig(self.p, text=pressure)

#TEST CODE
'''win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry("800x375")
win.configure(bg='black')

s = Solenoid(win, 'black', 1, 125, 125, True, True, True, True, '#41d94d', True, True, True, True)
s.getWidget().pack(side='bottom')
st = Stepper(win, 'black', 125, 125, True, True, True, True, '#41d94d', True, True, True, True)
st.getWidget().pack(side='top')
o = PressureSensor(win, 'black', 125, 125, True, True, True, True, '#41d94d', True, True, True, True)
o.getWidget().pack(side='top')

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