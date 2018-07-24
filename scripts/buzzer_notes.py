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

try:
	while True:
		if up == True:
			frequency *= sqrt(2)
		else:
			frequency /= sqrt(2)
		print frequency
		Buzz.ChangeFrequency(frequency)
		Buzz.start(50)
		time.sleep(0.1)
		Buzz.stop()
		
		if frequency < 5:
			up = True
		elif frequency > 25000:
			up = False
except KeyboardInterrupt:
	print '\nexiting'
