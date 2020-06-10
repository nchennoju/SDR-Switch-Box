#!/usr/bin python3
"""
SDRSwitchBoxUI2.py: A python GUI developed to interface with SDR rocketry's liquid engine switchbox.

    The interface consists of elements which write and read data to and from the Arduino to provide a
    fully interactive program. The program is meant to run on the launch computer which is hardwired
    to the arduino(s) via USB. Once the program is running, users are encouraged to move both windows as
    desired to fit their screen.

    Current Assumption: Arduino Uno -> Switchbox, Arduino Nano -> Data Logger
    ** Board type is used to find Arduino com ports automatically

    On one window, switch box relay controls will be present. Each switch widget on the GUI controls
    the corresponding relay within the switchbox. Additionally on the bottom of the window, gauge
    widgets provide realtime sensor readings.

    On another window, a graph of sensor readings are plotted and able to be logged into a .txt file
    for post- test analysis.

"""

__author__      = "Nitish Chennoju"
__credits__ = ["Colton Acosta"]

#GUI Imports
import tkinter as tk
import serial
import serial.tools.list_ports

#Custom Classes
import Gauge
import RelaySwitch

#Spacing constant within GUI
pad = 10

#Returns list of all accessible serial ports
def getPorts():
    portData = serial.tools.list_ports.comports()
    return portData
#Returns COM port of Arduino UNO if detected by computer. User for switchbox
def findArduino(portsFound):
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        if('Uno' in str(portsFound[i])):
            return str(portsFound[i])
    return "None"
#Returns COM port of Arduino Nano if detected by computer. Used for logger
def findArduino2(portsFound):
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        if('Nano' in str(portsFound[i]) or 'CH340' in str(portsFound[i])):
            return str(portsFound[i])
    return "None"


def startup():
    print("Startup")
    #can either be controlled via python program triggers event in arduino
    #Advantage of python: can see on GUI which relays are being triggered
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
test2 = findArduino2(getPorts())
if(test2 == "None"):
    arduinoLogger = serial.Serial()
    l3 = tk.Label(root, text="DISCONNECTED: " + test2, bg="black", fg="red", font="Arial 14 bold").pack()
else:
    arduinoLogger = serial.Serial(test2.split()[0], 115200)
    l3 = tk.Label(root, text="CONNECTED: " + test2, bg="black", fg="green2", font="Arial 14 bold").pack()

g1 = Gauge.Gauge(g, 'black', -30, 210)
g1.setText("AcX: NaN")
g1.getWidget().pack(side="left")
g2 = Gauge.Gauge(g, 'black', -30, 210)
g2.setText("AcY: NaN")
g2.getWidget().pack(side="left")
g3 = Gauge.Gauge(h, 'black', -30, 210)
g3.setText("AcZ: NaN")
g3.getWidget().pack(side="left")
g4 = Gauge.Gauge(h, 'black', -30, 210)
g4.setText("Tmp: NaN")
g4.getWidget().pack(side="right")
g.pack()
h.pack()

def removeStr(str, omit):
    a = str.index(omit)
    return float(str[a + len(omit):len(str)-1])

while test2 != "None":
    strSerial = arduinoLogger.readline().decode()
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
        g1.setText("AcX: " + data[1])
        g2.setAngle(abs(float(data[2])) * (180.0 / 10.0))
        g2.setText("AcY: " + data[2])
        g3.setAngle(abs(float(data[3])) * (180.0 / 10.0))
        g3.setText("AcZ: " + data[3])
        g4.setAngle(abs(float(data[9])) * (180.0 / 50.0))
        g4.setText("Tmp: " + data[9])

    root.update()


root.mainloop()