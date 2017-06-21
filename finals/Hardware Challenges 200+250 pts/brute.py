import serial

ser = serial.Serial('/dev/tty.usbmodem1421', 9600)

FINDME = "vI2QjIy8q7mEvZ6MzMnLoM6FoJeejZuC9f/="
PASS = ""
maxchar = ''
maxmatch = 0

while True:
	maxmatch = 0
	maxchar = ''
	for cn in range(32,127):
		testpass = PASS + chr(cn)
		ser.write(testpass+'\n')
		print testpass


CrossCTF{Bas364_1z_hard}

