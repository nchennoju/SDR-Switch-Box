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
import time
import threading
import asyncio
import tkinter as tk
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#Custom Classes
import Gauge
import RelaySwitch



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

def main():
    # Spacing constant within GUI
    pad = 10


    def startup():
        print("Startup")
        # can either be controlled via python program triggers event in arduino
        # Advantage of python: can see on GUI which relays are being triggered
        for i in range(10):
            switch1.on_button.invoke()
            time.sleep(0.5)
            switch1.off_button.invoke()
            switch2.on_button.invoke()
            time.sleep(0.5)
            switch2.off_button.invoke()

    def allOff():
        arduinoSwitchbox.write(b'8')
        switch1.off_button.select()
        switch2.off_button.select()
        switch3.off_button.select()
        switch4.off_button.select()
        switch1.lR.config(bg="red")
        switch2.lR.config(bg="red")
        switch3.lR.config(bg="red")
        switch4.lR.config(bg="red")
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

    l1 = tk.Label(root, text="SDR - Liquid Engine Dashboard", bg="black", fg="white", font="Arial 30 bold").pack(pady=60)

    test = findArduino(getPorts())
    if(test == "None"):
        arduinoSwitchbox = serial.Serial()
        l2 = tk.Label(root, text="DISCONNECTED: " + test, bg="black", fg="red", font="Arial 14 bold").pack()
    else:
        arduinoSwitchbox = serial.Serial(test.split()[0], 115200)
        l2 = tk.Label(root, text="CONNECTED: " + test, bg="black", fg="green2", font="Arial 14 bold").pack()
    print(test)

    #RELAY Switches created
    switch1 = RelaySwitch.Switch(root, "Relay 1: ", 0, arduinoSwitchbox)
    switch2 = RelaySwitch.Switch(root, "Relay 2: ", 1, arduinoSwitchbox)
    switch3 = RelaySwitch.Switch(root, "Relay 3: ", 2, arduinoSwitchbox)
    switch4 = RelaySwitch.Switch(root, "Relay 4: ", 3, arduinoSwitchbox)

    f = tk.Frame(root)
    g = tk.Frame(root)
    h = tk.Frame(root)
    s = tk.Button(f, text="STARTUP", padx=40, pady=10, font="Verdana 14 bold", bg="yellow", command=startup)
    off = tk.Button(f, text="All OFF", padx=30, pady=10, font="Verdana 14 bold", bg="RED", command=allOff)

    s.pack(side="left")
    off.pack(side="left")
    f.pack(pady=2*pad)




    #------------------------ DATA LOGGER -------------------------------
    g1 = Gauge.Gauge(g, 'black', -30, 210)
    g1.setText("Nan", "AcX")
    g1.getWidget().pack(side="left")
    g2 = Gauge.Gauge(g, 'black', -30, 210)
    g2.setText("Nan", "AcY")
    g2.getWidget().pack(side="left")
    g3 = Gauge.Gauge(h, 'black', -30, 210)
    g3.setText("Nan", "AcZ")
    g3.getWidget().pack(side="left")
    g4 = Gauge.Gauge(h, 'black', -30, 210)
    g4.setText("Nan", "Tmp")
    g4.getWidget().pack(side="right")
    g.pack()
    h.pack()


    while test != "None":
        strSerial = arduinoSwitchbox.readline().decode()
        data = strSerial.split("\t")

        if(data[0] == "Time"):
            file = open(fileName, "a")
            file.write(strSerial[0:len(strSerial) - 2] + "\n")
            print(strSerial[0:len(strSerial) - 2])
            file.close()
        elif(len(data) > 9 and data[0] != "Time"):
            file = open(fileName, "a")
            file.write(strSerial[0:len(strSerial) - 2] + "\n")
            print(strSerial[0:len(strSerial) - 2])
            file.close()
            g1.setAngle(abs(float(data[1])) * (180.0 / 10.0))
            g1.setText(data[1], "AcX")
            g2.setAngle(abs(float(data[2])) * (180.0 / 10.0))
            g2.setText(data[2], "AcY")
            g3.setAngle(abs(float(data[3])) * (180.0 / 10.0))
            g3.setText(data[3], "AcZ")
            g4.setAngle(abs(float(data[9])) * (180.0 / 50.0))
            g4.setText(data[9].replace('\n', ''), "Tmp")

        root.update()

    root.mainloop()


if __name__ == "__main__":
    main()