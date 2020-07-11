# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
import time
from random import randint
import tkinter as tk

import Nozzle
import Tank
import Valves
import Pipes
import Header

gridLen = 85

width = gridLen*8
height = gridLen*12

win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry(str(width) + "x" + str(height))
win.configure(bg='black')

win_w = width
win_h = height

#CONSTANT
fluidColor = '#41d94d'

#HEADER
header = Header.Header(win, 'black', 'SDR P&ID GUI', width, gridLen, 24)
header.getWidget().place(x=gridLen*0, y=gridLen*0)

#All TANKS
gn2 = Tank.Tank(win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
lox = Tank.Tank(win, 'black', 'LOx', '#1d2396', gridLen, gridLen)
k = Tank.Tank(win, 'black', 'K', '#1d2396', gridLen, gridLen)
gn2.getWidget().place(x=gridLen*3, y=gridLen*1)
lox.getWidget().place(x=gridLen*1, y=gridLen*5)
k.getWidget().place(x=gridLen*6, y=gridLen*5)

#All SOLENOID VALVES
one = Valves.Solenoid(win, 'black', 1, gridLen, gridLen, False, True, True, False, fluidColor, False, False, False, False)
two = Valves.Solenoid(win, 'black', 2, gridLen, gridLen, False, True, False, False, fluidColor, False, False, False, False)
three = Valves.Solenoid(win, 'black', 3, gridLen, gridLen, False, False, True, True, fluidColor, False, False, False, False)
four = Valves.Solenoid(win, 'black', 4, gridLen, gridLen, False, True, False, False, fluidColor, False, False, False, False)
five = Valves.Solenoid(win, 'black', 5, gridLen, gridLen, True, False, False, True, fluidColor, False, False, False, False)
six = Valves.Solenoid(win, 'black', 6, gridLen, gridLen, False, True, False, True, fluidColor, False, False, False, False)
one.getWidget().place(x=gridLen*1, y=gridLen*2)
two.getWidget().place(x=gridLen*0, y=gridLen*4)
three.getWidget().place(x=gridLen*6, y=gridLen*2)
four.getWidget().place(x=gridLen*5, y=gridLen*4)
five.getWidget().place(x=gridLen*3, y=gridLen*8)
six.getWidget().place(x=gridLen*4, y=gridLen*7)

#All STEPPER
s1 = Valves.Stepper(win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False, False, False, False)
s2 = Valves.Stepper(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False, False)
s1.getWidget().place(x=gridLen*6, y=gridLen*7)
s2.getWidget().place(x=gridLen*2, y=gridLen*8)

#All ORIFICES
o1 = Valves.Orifice(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False, False, False, False)
o2 = Valves.Orifice(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False, False)
o1.getWidget().place(x=gridLen*1, y=gridLen*6)
o2.getWidget().place(x=gridLen*5, y=gridLen*7)

#All Pressure Sensors
ps1 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d', False, False, False, False)
ps2 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False, False)
ps3 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, False, False, True, '#41d94d', False, False, False, False)
ps1.getWidget().place(x=gridLen*0, y=gridLen*3)
ps2.getWidget().place(x=gridLen*5, y=gridLen*9)
ps3.getWidget().place(x=gridLen*7, y=gridLen*3)

tp1 = Valves.TempSensor(win, 'black', gridLen, gridLen, True, False, False, False, '#41d94d', False, False, False, False)
tp1.getWidget().place(x=gridLen*5, y=gridLen*10)

#All Text boxes
t1 = Header.Text(win, 'black', 'K Fill', gridLen, gridLen, 12)
t2 = Header.Text(win, 'black', 'K Drain', gridLen, gridLen, 12)
t3 = Header.Text(win, 'black', 'LOx\nFill/Drain', gridLen, gridLen, 12)
t4 = Header.Text(win, 'black', 'Regen\nCircuit', gridLen, gridLen, 12)
t1.getWidget().place(x=gridLen*7, y=gridLen*4)
t2.getWidget().place(x=gridLen*7, y=gridLen*6)
t3.getWidget().place(x=gridLen*1, y=gridLen*9)
t4.getWidget().place(x=gridLen*7, y=gridLen*9)

#All PIPES
p1 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
p2 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
p3 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
p4 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
p5 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
p6 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p7 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
p8 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
p9 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p10 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
p11 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p12 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p13 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
p14 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p15 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
p16 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
p17 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
p18 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, False, True, True, '#41d94d', False)
p19 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
p20 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
p21 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
p22 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False)

p1.getWidget().place(x=gridLen*2, y=gridLen*2)
p2.getWidget().place(x=gridLen*3, y=gridLen*2)
p3.getWidget().place(x=gridLen*4, y=gridLen*2)
p4.getWidget().place(x=gridLen*5, y=gridLen*2)
p5.getWidget().place(x=gridLen*1, y=gridLen*3)
p6.getWidget().place(x=gridLen*3, y=gridLen*3)
p7.getWidget().place(x=gridLen*6, y=gridLen*3)
p8.getWidget().place(x=gridLen*1, y=gridLen*4)
p9.getWidget().place(x=gridLen*3, y=gridLen*4)
p10.getWidget().place(x=gridLen*6, y=gridLen*4)
p11.getWidget().place(x=gridLen*3, y=gridLen*5)
p12.getWidget().place(x=gridLen*3, y=gridLen*6)
p13.getWidget().place(x=gridLen*6, y=gridLen*6)
p14.getWidget().place(x=gridLen*1, y=gridLen*7)
p15.getWidget().place(x=gridLen*3, y=gridLen*7)
p16.getWidget().place(x=gridLen*1, y=gridLen*8)
p17.getWidget().place(x=gridLen*5, y=gridLen*8)
p18.getWidget().place(x=gridLen*6, y=gridLen*8)
p19.getWidget().place(x=gridLen*2, y=gridLen*9)
p20.getWidget().place(x=gridLen*3, y=gridLen*9)
p21.getWidget().place(x=gridLen*4, y=gridLen*9)
p22.getWidget().place(x=gridLen*6, y=gridLen*9)

#NOZZLE
n = Nozzle.Nozzle(win, 'black', gridLen, gridLen*1.5)
n.getWidget().place(x=gridLen*3, y=gridLen*10)

win.mainloop()