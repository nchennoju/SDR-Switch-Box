import tkinter as tk
import serial
import serial.tools.list_ports
import time

pad = 10;

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
    state = switch_variable1.get();
    if(state == "on"):
        arduino.write(11);
    elif(state == "off"):
        arduino.write(10);
def action2():
    state = switch_variable1.get();
    if(state == "on"):
        arduino.write(21);
    elif(state == "off"):
        arduino.write(20);
def action3():
    state = switch_variable1.get();
    if(state == "on"):
        arduino.write(31);
    elif(state == "off"):
        arduino.write(30);
def action4():
    state = switch_variable1.get();
    if(state == "on"):
        arduino.write(41);
    elif(state == "off"):
        arduino.write(40);


#CODE START
test = findArduino(getPorts())
if(test != "None"):
    arduino = serial.Serial(test.split()[0], baudrate=115200, timeout=1)
    time.sleep(1)
print(test)

root = tk.Tk()
root.title("SDR - Liquid Engine Dashboard");
root.configure(background = "black")
root.geometry("750x500");

#l1 = tk.Label(root, text="SDR - Liquid Engine Dashboard", bg="black", fg="white", font="Arial 16 bold").grid(row=0, column=0)
l1 = tk.Label(root, text="SDR - Liquid Engine Dashboard", bg="black", fg="white", font="Arial 30 bold").pack(pady=60)
if(test == "None"):
    #l2 = tk.Label(root, text="DISCONNECTED: " + test, bg="black", fg="red", font="Arial 10 bold").grid(row=1, column=0)
    l2 = tk.Label(root, text="DISCONNECTED: " + test, bg="black", fg="red", font="Arial 14 bold").pack()
else:
    #l2 = tk.Label(root, text="CONNECTED: " + test, bg="black", fg="green2", font="Arial 10 bold").grid(row=1, column=0)
    l2 = tk.Label(root, text="CONNECTED: " + test, bg="black", fg="green2", font="Arial 14 bold").pack()
#RELAY 1 Control
switchR1 = tk.Frame(root)
lR1 = tk.Label(switchR1, text="Relay 1: ", bg="black", fg="white", font="Arial 16 bold")
switch_variable1 = tk.StringVar(value="off")
off_button = tk.Radiobutton(switchR1, text="OFF", variable=switch_variable1,indicatoron=False, value="off", width=12, command=action1)
on_button = tk.Radiobutton(switchR1, text="ON", variable=switch_variable1,indicatoron=False, value="on", width=12, command=action1)
lR1.pack(side="left")
off_button.pack(side="left")
on_button.pack(side="left")

#switchR1.grid(row=2, column=0)
switchR1.pack(pady=pad)



#RELAY 2 Control
switchR2 = tk.Frame(root)
lR2 = tk.Label(switchR2, text="Relay 2: ", bg="black", fg="white", font="Arial 16 bold")
switch_variable2 = tk.StringVar(value="off")
off_button = tk.Radiobutton(switchR2, text="OFF", variable=switch_variable2,indicatoron=False, value="off", width=12, command=action2)
on_button = tk.Radiobutton(switchR2, text="ON", variable=switch_variable2,indicatoron=False, value="on", width=12, command=action2)
lR2.pack(side="left")
off_button.pack(side="left")
on_button.pack(side="left")

#switchR2.grid(row=3, column=0)
switchR2.pack(pady=pad)

#RELAY 3 Control
switchR3 = tk.Frame(root)
lR3 = tk.Label(switchR3, text="Relay 3: ", bg="black", fg="white", font="Arial 16 bold")
switch_variable3 = tk.StringVar(value="off")
off_button = tk.Radiobutton(switchR3, text="OFF", variable=switch_variable3,indicatoron=False, value="off", width=12, command=action3)
on_button = tk.Radiobutton(switchR3, text="ON", variable=switch_variable3,indicatoron=False, value="on", width=12, command=action3)
lR3.pack(side="left")
off_button.pack(side="left")
on_button.pack(side="left")

#switchR3.grid(row=4, column=0)
switchR3.pack(pady=pad)

#RELAY 4 Control
switchR4 = tk.Frame(root)
lR4 = tk.Label(switchR4, text="Relay 4: ", bg="black", fg="white", font="Arial 16 bold")
switch_variable4 = tk.StringVar(value="off")
off_button = tk.Radiobutton(switchR4, text="OFF", variable=switch_variable4,indicatoron=False, value="off", width=12, command=action4)
on_button = tk.Radiobutton(switchR4, text="ON", variable=switch_variable4,indicatoron=False, value="on", width=12, command=action4)
lR4.pack(side="left")
off_button.pack(side="left")
on_button.pack(side="left")

#switchR4.grid(row=5, column=0)
switchR4.pack(pady=pad)

root.mainloop()