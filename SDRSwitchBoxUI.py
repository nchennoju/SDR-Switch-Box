import tkinter as tk
import serial
import serial.tools.list_ports
import time


def getPorts():
    portData = serial.tools.list_ports.comports()
    return portData

def findArduino(portsFound):
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        if('Arduino' in str(portsFound[i]) or 'CH340' in str(portsFound[i])):
            return str(portsFound[i])
    return "None"


def action1():
    arduino.write(1);
    print("Relay 1 Trigerred")
def action2():
    arduino.write(2);
    print("Relay 2 Trigerred")
def action3():
    arduino.write(3);
    print("Relay 3 Trigerred")
def action4():
    arduino.write(4);
    print("Relay 4 Trigerred")
def startup():
    arduino.write(-2);
    print("start")
def off():
    arduino.write(-1);
    print("all off")


#CODE START
test = findArduino(getPorts())
if(test != "None"):
    arduino = serial.Serial(test.split()[0], baudrate=115200, timeout=1)
    time.sleep(1)

root = tk.Tk()
root.title("SDR - Liquid Engine Dashboard");
root.configure(background = "black")

l1 = tk.Label(root, text="SDR - Liquid Engine Dashboard", bg="black", fg="white", font="Arial 16 bold").grid(row=0, column=0)
if(test == "None"):
    l2 = tk.Label(root, text="DISCONNECTED: " + test, bg="black", fg="red", font="Arial 10 bold").grid(row=1, column=0)
else:
    l2 = tk.Label(root, text="CONNECTED: " + test, bg="black", fg="green2", font="Arial 10 bold").grid(row=1, column=0)
b1 = tk.Button(root, text="Relay#1", padx=15, pady=5, command=action1).grid(row=2, column=0)
b2 = tk.Button(root, text="Relay#2", padx=15, pady=5, command=action2).grid(row=3, column=0)
b3 = tk.Button(root, text="Relay#3", padx=15, pady=5, command=action3).grid(row=4, column=0)
b4 = tk.Button(root, text="Relay#4", padx=15, pady=5, command=action4).grid(row=5, column=0)
s = tk.Button(root, text="STARTUP", padx=15, pady=5, command=startup).grid(row=6, column=0)
o = tk.Button(root, text="--OFF--", padx=20, pady=7, command=off).grid(row=7, column=0)

root.mainloop()