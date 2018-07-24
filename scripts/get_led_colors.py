import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random

colors = ['M', 'R', 'G', 'C', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

i = 0

try:
	while True:
		LED.setColor(colors[i])
		time.sleep(0.03)
		i = (i+1)%len(colors)
	# n = random.randint(0,3)
	# LED.setColor(colors[n])
	# time.sleep(0.5)
except:
	print "closing program"
LED.noColor()
time.sleep(0.5)
LED.destroy()
