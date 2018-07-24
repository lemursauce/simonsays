import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

frequency = 27.5
up = True

factor = 2.0**(1.0/12)

try:
	while True:
		print frequency
		Buzz.ChangeFrequency(int(frequency))
		Buzz.start(50)
		time.sleep(0.15)
		Buzz.stop()

		if up == True:
			frequency *= factor
		else:
			frequency /= factor
		
		if frequency < 28:
			up = True
			print 'going up'
		elif frequency > 24000:
			up = False
			print 'going down'
except KeyboardInterrupt:
	print '\nexiting'
