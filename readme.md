This GUI program is capable of controlling the SDR Liquid Engine Switchbox to:
1) Automate Liquid Engine Startup
2) Display and Log Datalogger values

# GUI Layout
![Switchbox](https://github.com/nchennoju/SDR-Switch-Box/blob/master/IMG-2598.jpg)


A couple things to keep in mind:

Boards required for com port auto detection:
	Arduino UNO - Switch box
		- consists of Arduino Uno controlling relay board
	Arduino NANO / CH340 - Data Logger
		- data logger has capability to log data onboard to SD card


Current IMPORTS:
import tkinter as tk
import serial
import serial.tools.list_ports
#import matplotlib.pyplot as plt


Install the following modules: (type in command)
pip install pyserial
pip install matplotlib
