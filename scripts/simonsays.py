import RPi.GPIO as GPIO
import LEDRGB as LED
from getpass import getpass
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

Cont = True

def rand():
	n = random.randint(0,len(colors)-1)
	seq.append(colors[n])
	seqS.append(sounds[n])

if __name__ == '__main__':
	try:
		while Cont:
			n = rand()
			for i in range(len(seq)):
				LED.setColor(seq[i])
				Buzz.ChangeFrequency(seqS[i])
				Buzz.start(50)
				time.sleep(.25)

				LED.noColor()
				Buzz.stop()
				if i < len(seq)-1:
					time.sleep(.25)
			
			#user input
			c = getpass("level " + str(len(seq)))
			if not c.upper() == ''.join(seq):
				print "INCORRECT\n"
				print "your guess was:", ', '.join(list(c.upper()))
				print "\nThe correct sequence was:", ', '.join(seq)
				print "\nYou made it to level", len(seq)
				Cont = False
				break
		#
	except:
		print "\nGood Bye"

LED.noColor()
LED.destroy()
