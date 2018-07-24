import RPi.GPIO as GPIO
import LEDRGB as LED

import time
import random

colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

def rand():
	while True:
		n = random.randint(0,len(colors)-1)
		LED.setColor(colors[n])
		time.sleep(.2)

if __name__ == '__main__':
	try:
		rand()
	except KeyboardInterrupt:
		LED.noColor()
		time.sleep(0.5)
		LED.destroy()
		print "Good Bye"
