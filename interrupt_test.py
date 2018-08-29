import RPi.GPIO as GPIO
import time

INPUT0 = 16
INPUT1 = 20
INPUT2 = 21



#counter_0 = 0
#lasttime_0 = time.time()

#GPIO.setup(INPUT0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(INPUT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(INPUT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#def processPulse(channel, status):

def gpioCallback(channel):
	if(channel == INPUT0):
		global input0
		print("channel:" + str(channel) + ", counter:" + str(input0.counter))
		input0.counter += 1
		
class RInput:
	def __init__(self, number):
		self.number = number
		self.counter = 0
		self.lasttime = time.time()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(number, GPIO.FALLING, callback=gpioCallback, bouncetime=200)
		print("RInput:" + str(number) + " created.")

	
input0 = RInput(INPUT0);

while True:
	time.sleep(1)
