import serial, time

ser = serial.Serial('/dev/tty.usbmodem1421', 9600)

time.sleep(2)
ser.write("CrossCTF{Bas364_1z_hard}\n")

while True:
	ser.readline()
	time.sleep(1)