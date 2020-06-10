import tkinter as tk

pad = 10

class Switch:

    def __init__(self, root, name, pinNum, arduino):
        self.arduino = arduino

        self.name = name
        self.pinNum = pinNum

        self.switch = tk.Frame(root)
        self.lR = tk.Label(self.switch, text=name, bg="red", fg="white", font="Arial 16 bold")
        self.state = tk.StringVar(value=0)
        self.off_button = tk.Radiobutton(self.switch, text="OFF", variable=self.state, indicatoron=False, value=0, width=12, command=self.action)
        self.on_button = tk.Radiobutton(self.switch, text="ON", variable=self.state, indicatoron=False, value=1, width=12, command=self.action)
        self.lR.pack(side="left")
        self.off_button.pack(side="left")
        self.on_button.pack(side="left")
        self.switch.pack(pady=pad)

    def action(self):
        serialNum = (self.pinNum*2) + int(self.state.get())
        if (serialNum%2 == 1):
            self.lR.config(bg="green2")
        elif (serialNum%2 == 0):
            self.lR.config(bg="red")
        self.arduino.write(str.encode(str(serialNum)))
        print(str(serialNum))