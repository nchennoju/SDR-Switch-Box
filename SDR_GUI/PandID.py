import tkinter as tk

import Nozzle
import Tank
import Valves
import Pipes
import Header


class Engine_Plumbing:

    def __init__(self, gridLen):
        width = gridLen * 8
        height = gridLen * 12

        self.win = tk.Tk()
        self.win.title("P&ID Diagram")
        self.win.geometry(str(width) + "x" + str(height))
        self.win.configure(bg='black')

        # CONSTANT
        fluidColor = '#41d94d'

        # HEADER
        self.header = Header.Header(self.win, 'black', 'SDR P&ID GUI', width, gridLen, 24)
        self.header.getWidget().place(x=gridLen * 0, y=gridLen * 0)

        # All TANKS
        self.gn2 = Tank.Tank(self.win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
        self.lox = Tank.Tank(self.win, 'black', 'LOx', '#1d2396', gridLen, gridLen)
        self.k = Tank.Tank(self.win, 'black', 'K', '#1d2396', gridLen, gridLen)
        self.gn2.getWidget().place(x=gridLen * 3, y=gridLen * 1)
        self.lox.getWidget().place(x=gridLen * 1, y=gridLen * 5)
        self.k.getWidget().place(x=gridLen * 6, y=gridLen * 5)

        # All SOLENOID VALVES
        self.one = Valves.Solenoid(self.win, 'black', 1, gridLen, gridLen, False, True, True, False, fluidColor)
        self.two = Valves.Solenoid(self.win, 'black', 2, gridLen, gridLen, False, True, False, False, fluidColor)
        self.three = Valves.Solenoid(self.win, 'black', 3, gridLen, gridLen, False, False, True, True, fluidColor)
        self.four = Valves.Solenoid(self.win, 'black', 4, gridLen, gridLen, False, True, False, False, fluidColor)
        self.five = Valves.Solenoid(self.win, 'black', 5, gridLen, gridLen, True, False, False, True, fluidColor)
        self.six = Valves.Solenoid(self.win, 'black', 6, gridLen, gridLen, False, True, False, True, fluidColor)
        self.one.getWidget().place(x=gridLen * 1, y=gridLen * 2)
        self.two.getWidget().place(x=gridLen * 0, y=gridLen * 4)
        self.three.getWidget().place(x=gridLen * 6, y=gridLen * 2)
        self.four.getWidget().place(x=gridLen * 5, y=gridLen * 4)
        self.five.getWidget().place(x=gridLen * 3, y=gridLen * 8)
        self.six.getWidget().place(x=gridLen * 4, y=gridLen * 7)

        # All STEPPER
        self.s1 = Valves.Stepper(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False, False, False,
                            False)
        self.s2 = Valves.Stepper(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False,
                            False)
        self.s1.getWidget().place(x=gridLen * 6, y=gridLen * 7)
        self.s2.getWidget().place(x=gridLen * 2, y=gridLen * 8)

        # All ORIFICES
        self.o1 = Valves.Orifice(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False, False, False,
                            False)
        self.o2 = Valves.Orifice(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False,
                            False)
        self.o1.getWidget().place(x=gridLen * 1, y=gridLen * 6)
        self.o2.getWidget().place(x=gridLen * 5, y=gridLen * 7)

        # All Pressure Sensors
        self.ps1 = Valves.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d', False, False,
                                    False, False)
        self.ps2 = Valves.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False,
                                    False,
                                    False)
        self.ps3 = Valves.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, False, True, '#41d94d', False, False,
                                    False, False)
        self.ps1.getWidget().place(x=gridLen * 0, y=gridLen * 3)
        self.ps2.getWidget().place(x=gridLen * 5, y=gridLen * 9)
        self.ps3.getWidget().place(x=gridLen * 7, y=gridLen * 3)

        self.tp1 = Valves.TempSensor(self.win, 'black', gridLen, gridLen, True, False, False, False, '#41d94d', False, False,
                                False,
                                False)
        self.tp1.getWidget().place(x=gridLen * 5, y=gridLen * 10)

        # All Text boxes
        self.t1 = Header.Text(self.win, 'black', 'K Fill', gridLen, gridLen, 12)
        self.t2 = Header.Text(self.win, 'black', 'K Drain', gridLen, gridLen, 12)
        self.t3 = Header.Text(self.win, 'black', 'LOx\nFill/Drain', gridLen, gridLen, 12)
        self.t4 = Header.Text(self.win, 'black', 'Regen\nCircuit', gridLen, gridLen, 12)
        self.t1.getWidget().place(x=gridLen * 7, y=gridLen * 4)
        self.t2.getWidget().place(x=gridLen * 7, y=gridLen * 6)
        self.t3.getWidget().place(x=gridLen * 1, y=gridLen * 9)
        self.t4.getWidget().place(x=gridLen * 7, y=gridLen * 9)

        # All PIPES
        self.p1 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p2 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p3 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p4 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p5 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
        self.p6 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p7 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p8 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
        self.p9 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p10 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p11 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p12 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p13 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p14 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p15 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p16 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p17 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p18 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, False, True, True, '#41d94d', False)
        self.p19 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p20 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
        self.p21 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p22 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False)
        self.p1.getWidget().place(x=gridLen * 2, y=gridLen * 2)
        self.p2.getWidget().place(x=gridLen * 3, y=gridLen * 2)
        self.p3.getWidget().place(x=gridLen * 4, y=gridLen * 2)
        self.p4.getWidget().place(x=gridLen * 5, y=gridLen * 2)
        self.p5.getWidget().place(x=gridLen * 1, y=gridLen * 3)
        self.p6.getWidget().place(x=gridLen * 3, y=gridLen * 3)
        self.p7.getWidget().place(x=gridLen * 6, y=gridLen * 3)
        self.p8.getWidget().place(x=gridLen * 1, y=gridLen * 4)
        self.p9.getWidget().place(x=gridLen * 3, y=gridLen * 4)
        self.p10.getWidget().place(x=gridLen * 6, y=gridLen * 4)
        self.p11.getWidget().place(x=gridLen * 3, y=gridLen * 5)
        self.p12.getWidget().place(x=gridLen * 3, y=gridLen * 6)
        self.p13.getWidget().place(x=gridLen * 6, y=gridLen * 6)
        self.p14.getWidget().place(x=gridLen * 1, y=gridLen * 7)
        self.p15.getWidget().place(x=gridLen * 3, y=gridLen * 7)
        self.p16.getWidget().place(x=gridLen * 1, y=gridLen * 8)
        self.p17.getWidget().place(x=gridLen * 5, y=gridLen * 8)
        self.p18.getWidget().place(x=gridLen * 6, y=gridLen * 8)
        self.p19.getWidget().place(x=gridLen * 2, y=gridLen * 9)
        self.p20.getWidget().place(x=gridLen * 3, y=gridLen * 9)
        self.p21.getWidget().place(x=gridLen * 4, y=gridLen * 9)
        self.p22.getWidget().place(x=gridLen * 6, y=gridLen * 9)

        # NOZZLE
        self.n = Nozzle.Nozzle(self.win, 'black', gridLen, gridLen * 1.5)
        self.n.getWidget().place(x=gridLen * 3, y=gridLen * 10)

        self.s2.setNeighbors(None, self.five, self.p19, self.p16)
        self.s1.setNeighbors(self.p13, None, None, self.o2)

    def getWindow(self):
        return self.win

