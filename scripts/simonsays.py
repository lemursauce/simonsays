import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

colors = ['R', 'G', 'B', 'Y']

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

sounds = [220,311.13,440,662.25]

seq = []
seqS = []

def rand():
	n = random.randint(0,len(colors)-1)
	seq.append(colors[n])
	seqS.append(sounds[n])

if __name__ == '__main__':
	try:
		while True:
			n = rand()
			for i in range(len(seq)):
				LED.setColor(seq[i])
				Buzz.ChangeFrequency(seqS[i])
				Buzz.start(50)
				time.sleep(.25)

				LED.noColor()
				Buzz.stop()
				time.sleep(.25)
			time.sleep(.75)
	except KeyboardInterrupt:
		LED.noColor()
		LED.destroy()
		print "Good Bye"
