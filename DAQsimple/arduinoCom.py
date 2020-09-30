####### arduinoCom Module: Functions for Arduino Communications 

# Arduino imports
import serial
import serial.tools.list_ports as list_ports 


## getPorts: 
## Returns list of accesible serial ports
def getPorts():
	portData = list_ports.comports()
	return portData 

## findArduinoUno:
## Input: list of accesible ports
## Output: COM port of Arduino Uno as String
def findArduinoUno(ports):
	for port in ports:
		if ('Uno' in str(port)):
			return str(port)
	return "None"

## findArduinoNano
## Input: list of accesible ports
def findArduinoNano(ports):
	for port in ports:
		if ('CH340' in str(port)):
			return str(port)
		else:
			return "None"

## getData:
## Output: Serial Data Point
def getData(serialData):
	Data = serialData.readline().decode('ascii')
	return str(Data)


