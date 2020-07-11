#!/usr/bin python3
"""
SDRSwitchBoxUI2.py: A python GUI developed to interface with SDR rocketry's liquid engine switchbox.

    The interface consists of elements which write and read data to and from the Arduino to provide a
    fully interactive program. The program is meant to run on the launch computer which is hardwired
    to the switchbox arduino via USB. Once the program is running, users are encouraged to move the
    window to fit their needs.

    Current Assumption:
    ** Board type is an Arduino Nano or Uno (used to find Arduino com ports automatically)

    On the window, switch box relay controls will be present along with a series of Gauge objects
    which display sensor readings. Additionally, all realtime sensor readings are logged onto a .txt
    file onto the computer running the python script.

"""

__author__      = "Nitish Chennoju"
__credits__ = ["Colton Acosta"]

#GUI Imports
import serial
import serial.tools.list_ports

#Custom Classes
import Gauge
import RelaySwitch
import time
from random import randint
import tkinter as tk

import Nozzle
import Tank
import Valves
import Pipes
import Header



# Returns list of all accessible serial ports
def getPorts():
    portData = serial.tools.list_ports.comports()
    return portData

    # Returns COM port of Arduino if detected by computer. User for switchbox
def findArduino(portsFound):
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        if ('Uno' in str(portsFound[i]) or 'Nano' in str(portsFound[i]) or 'CH340' in str(portsFound[i])):
            return str(portsFound[i])
    return "None"

def conv(str):
    return str[2:len(str)-5]

def main():
    # Spacing constant within GUI
    pad = 10

    gridLen = 85

    width = gridLen * 8
    height = gridLen * 12

    win = tk.Tk()
    win.title("ELEMENT TEST")
    win.geometry(str(width) + "x" + str(height))
    win.configure(bg='black')

    # CONSTANT
    fluidColor = '#41d94d'

    # HEADER
    header = Header.Header(win, 'black', 'SDR P&ID GUI', width, gridLen, 24)
    header.getWidget().place(x=gridLen * 0, y=gridLen * 0)

    # All TANKS
    gn2 = Tank.Tank(win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
    lox = Tank.Tank(win, 'black', 'LOx', '#1d2396', gridLen, gridLen)
    k = Tank.Tank(win, 'black', 'K', '#1d2396', gridLen, gridLen)
    gn2.getWidget().place(x=gridLen * 3, y=gridLen * 1)
    lox.getWidget().place(x=gridLen * 1, y=gridLen * 5)
    k.getWidget().place(x=gridLen * 6, y=gridLen * 5)

    # All SOLENOID VALVES
    one = Valves.Solenoid(win, 'black', 1, gridLen, gridLen, False, True, True, False, fluidColor, False, False, False,
                          False)
    two = Valves.Solenoid(win, 'black', 2, gridLen, gridLen, False, True, False, False, fluidColor, False, False, False,
                          False)
    three = Valves.Solenoid(win, 'black', 3, gridLen, gridLen, False, False, True, True, fluidColor, False, False,
                            False, False)
    four = Valves.Solenoid(win, 'black', 4, gridLen, gridLen, False, True, False, False, fluidColor, False, False,
                           False, False)
    five = Valves.Solenoid(win, 'black', 5, gridLen, gridLen, True, False, False, True, fluidColor, False, False, False,
                           False)
    six = Valves.Solenoid(win, 'black', 6, gridLen, gridLen, False, True, False, True, fluidColor, False, False, False,
                          False)
    one.getWidget().place(x=gridLen * 1, y=gridLen * 2)
    two.getWidget().place(x=gridLen * 0, y=gridLen * 4)
    three.getWidget().place(x=gridLen * 6, y=gridLen * 2)
    four.getWidget().place(x=gridLen * 5, y=gridLen * 4)
    five.getWidget().place(x=gridLen * 3, y=gridLen * 8)
    six.getWidget().place(x=gridLen * 4, y=gridLen * 7)

    # All STEPPER
    s1 = Valves.Stepper(win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False, False, False, False)
    s2 = Valves.Stepper(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False, False)
    s1.getWidget().place(x=gridLen * 6, y=gridLen * 7)
    s2.getWidget().place(x=gridLen * 2, y=gridLen * 8)

    # All ORIFICES
    o1 = Valves.Orifice(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False, False, False, False)
    o2 = Valves.Orifice(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False, False)
    o1.getWidget().place(x=gridLen * 1, y=gridLen * 6)
    o2.getWidget().place(x=gridLen * 5, y=gridLen * 7)

    # All Pressure Sensors
    ps1 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d', False, False,
                                False, False)
    ps2 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False,
                                False)
    ps3 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, False, False, True, '#41d94d', False, False,
                                False, False)
    ps1.getWidget().place(x=gridLen * 0, y=gridLen * 3)
    ps2.getWidget().place(x=gridLen * 5, y=gridLen * 9)
    ps3.getWidget().place(x=gridLen * 7, y=gridLen * 3)

    tp1 = Valves.TempSensor(win, 'black', gridLen, gridLen, True, False, False, False, '#41d94d', False, False, False,
                            False)
    tp1.getWidget().place(x=gridLen * 5, y=gridLen * 10)

    # All Text boxes
    t1 = Header.Text(win, 'black', 'K Fill', gridLen, gridLen, 12)
    t2 = Header.Text(win, 'black', 'K Drain', gridLen, gridLen, 12)
    t3 = Header.Text(win, 'black', 'LOx\nFill/Drain', gridLen, gridLen, 12)
    t4 = Header.Text(win, 'black', 'Regen\nCircuit', gridLen, gridLen, 12)
    t1.getWidget().place(x=gridLen * 7, y=gridLen * 4)
    t2.getWidget().place(x=gridLen * 7, y=gridLen * 6)
    t3.getWidget().place(x=gridLen * 1, y=gridLen * 9)
    t4.getWidget().place(x=gridLen * 7, y=gridLen * 9)

    # All PIPES
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

    p1.getWidget().place(x=gridLen * 2, y=gridLen * 2)
    p2.getWidget().place(x=gridLen * 3, y=gridLen * 2)
    p3.getWidget().place(x=gridLen * 4, y=gridLen * 2)
    p4.getWidget().place(x=gridLen * 5, y=gridLen * 2)
    p5.getWidget().place(x=gridLen * 1, y=gridLen * 3)
    p6.getWidget().place(x=gridLen * 3, y=gridLen * 3)
    p7.getWidget().place(x=gridLen * 6, y=gridLen * 3)
    p8.getWidget().place(x=gridLen * 1, y=gridLen * 4)
    p9.getWidget().place(x=gridLen * 3, y=gridLen * 4)
    p10.getWidget().place(x=gridLen * 6, y=gridLen * 4)
    p11.getWidget().place(x=gridLen * 3, y=gridLen * 5)
    p12.getWidget().place(x=gridLen * 3, y=gridLen * 6)
    p13.getWidget().place(x=gridLen * 6, y=gridLen * 6)
    p14.getWidget().place(x=gridLen * 1, y=gridLen * 7)
    p15.getWidget().place(x=gridLen * 3, y=gridLen * 7)
    p16.getWidget().place(x=gridLen * 1, y=gridLen * 8)
    p17.getWidget().place(x=gridLen * 5, y=gridLen * 8)
    p18.getWidget().place(x=gridLen * 6, y=gridLen * 8)
    p19.getWidget().place(x=gridLen * 2, y=gridLen * 9)
    p20.getWidget().place(x=gridLen * 3, y=gridLen * 9)
    p21.getWidget().place(x=gridLen * 4, y=gridLen * 9)
    p22.getWidget().place(x=gridLen * 6, y=gridLen * 9)

    # NOZZLE
    n = Nozzle.Nozzle(win, 'black', gridLen, gridLen * 1.5)
    n.getWidget().place(x=gridLen * 3, y=gridLen * 10)


    def startup():
        print("Startup")

    def allOff():
        arduinoSwitchbox.write(b'8')
        switch1.setLedState(False)
        switch2.setLedState(False)
        switch3.setLedState(False)
        switch4.setLedState(False)
        switch5.setLedState(False)
        switch6.setLedState(False)
        switch7.setLedState(False)
        switch8.setLedState(False)
        print("All OFF COMPLETE")

    #MAIN CODE START
    print("Enter file name (don't include file extension): ", end='')
    fileName = input() + ".txt"




    #Initialize GUI Window
    root = tk.Tk()
    width = int(root.winfo_screenwidth())
    height = int(root.winfo_screenheight())
    dim = str(height) + "x" + str(width)
    root.title("SDR - Liquid Engine Dashboard");
    root.configure(background = "black")
    root.geometry(dim)

    tk.Label(root, text="SDR - Liquid Engine Dashboard", bg="black", fg="white", font="Arial 30").pack(pady=40)

    test = findArduino(getPorts())
    if(test == "None"):
        arduinoSwitchbox = serial.Serial()
        tk.Label(root, text="DISCONNECTED: " + test, bg="black", fg="red", font="Arial 14").pack()
    else:
        arduinoSwitchbox = serial.Serial(test.split()[0], 115200)
        tk.Label(root, text="CONNECTED: " + test, bg="black", fg="green2", font="Arial 14").pack()
    print(test)

    #RELAY Switches created
    a = tk.Frame(root, bg='black')
    b = tk.Frame(root, bg='black')
    c = tk.Frame(root, bg='black')
    d = tk.Frame(root, bg='black')
    switch1 = RelaySwitch.Buttons(a, 0, arduinoSwitchbox, "Relay 1", 60,
                                  60, one)  # RelaySwitch.Switch(root, "Relay 1: ", 0, arduinoSwitchbox)
    switch2 = RelaySwitch.Buttons(b, 1, arduinoSwitchbox, "Relay 2", 60,
                                  60, two)  # RelaySwitch.Switch(root, "Relay 2: ", 1, arduinoSwitchbox)
    switch3 = RelaySwitch.Buttons(c, 2, arduinoSwitchbox, "Relay 3", 60,
                                  60, three)  # RelaySwitch.Switch(root, "Relay 3: ", 2, arduinoSwitchbox)
    switch4 = RelaySwitch.Buttons(d, 3, arduinoSwitchbox, "Relay 4", 60,
                                  60, four)  # RelaySwitch.Switch(root, "Relay 4: ", 3, arduinoSwitchbox)
    switch5 = RelaySwitch.Buttons(a, 0, arduinoSwitchbox, "Relay 1", 60,
                                  60, five)  # RelaySwitch.Switch(root, "Relay 1: ", 0, arduinoSwitchbox)
    switch6 = RelaySwitch.Buttons(b, 1, arduinoSwitchbox, "Relay 2", 60,
                                  60, six)  # RelaySwitch.Switch(root, "Relay 2: ", 1, arduinoSwitchbox)
    #REPLACE
    switch7 = RelaySwitch.Buttons(c, 2, arduinoSwitchbox, "Relay 3", 60, 60, one)  # RelaySwitch.Switch(root, "Relay 3: ", 2, arduinoSwitchbox)
    switch8 = RelaySwitch.Buttons(d, 3, arduinoSwitchbox, "Relay 4", 60, 60, two)  # RelaySwitch.Switch(root, "Relay 4: ", 3, arduinoSwitchbox)

    a.pack()
    b.pack()
    c.pack()
    d.pack()

    g = tk.Frame(root)
    h = tk.Frame(root)
    s = tk.Button(root, text="STARTUP", padx=40, pady=10, font="Verdana 14", bg="yellow", command=startup, activebackground="yellow")
    off = tk.Button(root, text="All OFF", padx=30, pady=10, font="Verdana 14", bg="RED", command=allOff, activebackground="RED")

    s.pack(pady=pad)
    off.pack(pady=pad)


    #------------------------ DATA LOGGER -------------------------------
    g1 = Gauge.Gauge(g, 'black', -30, 210)
    g1.setText("Nan", "A0")
    g1.getWidget().pack(side="left")
    g2 = Gauge.Gauge(g, 'black', -30, 210)
    g2.setText("Nan", "A1")
    g2.getWidget().pack(side="left")
    g3 = Gauge.Gauge(h, 'black', -30, 210)
    g3.setText("Nan", "A2")
    g3.getWidget().pack(side="left")
    g4 = Gauge.Gauge(h, 'black', -30, 210)
    g4.setText("Nan", "A3")
    g4.getWidget().pack(side="right")
    g.pack()
    h.pack()


    while test != "None":
        strSerial = conv(str(arduinoSwitchbox.readline()))
        data = strSerial.split("\\t")

        if(data[0] == "Time"):
            file = open(fileName, "a")
            file.write(strSerial[0:len(strSerial) - 2] + "\n")
            print(strSerial[0:len(strSerial) - 2])
            file.close()
        elif(len(data) > 4 and data[0] != "Time"):
            file = open(fileName, "a")
            file.write(strSerial[0:len(strSerial) - 2] + "\n")
            print(strSerial[0:len(strSerial) - 2])
            file.close()
            g1.setAngle(abs(float(data[1])) * (180.0 / 1023.0))
            g1.setText(data[1], "A0")
            g2.setAngle(abs(float(data[2])) * (180.0 / 1023.0))
            g2.setText(data[2], "A1")
            g3.setAngle(abs(float(data[3])) * (180.0 / 1023.0))
            g3.setText(data[3], "A2")
            g4.setAngle(abs(float(data[4])) * (180.0 / 1023.0))
            g4.setText(data[4].replace('\n', ''), "A3")

        root.update()
        win.update()

    root.mainloop()
    win.mainloop()


if __name__ == "__main__":
    main()