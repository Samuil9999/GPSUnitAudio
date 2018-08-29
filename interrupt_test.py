import RPi.GPIO as GPIO
import time
from threading import Timer

INPUT0 = 16
INPUT1 = 20
INPUT2 = 21


def gpioCallback(channel):
	if(channel == INPUT0):
		global input0
		print("channel:" + str(channel) + ", counter:" + str(input0.counter))
		input0.processInterrupt()
	elif (channel == INPUT1):
		global input1
		print("channel:" + str(channel) + ", counter:" + str(input1.counter))
	elif (channel == INPUT2):
		global input2
		print("channel:" + str(channel) + ", counter:" + str(input2.counter))
		
class RInput:
	def __init__(self, number, pulselength):
		self.number = number
		self.pulselength = pulselength
		self.counter = 0
		self.lasttime = time.time()
		self.delta = 0
		self.initTimer()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(number, GPIO.BOTH, callback=gpioCallback, bouncetime=100)
		print("RInput:" + str(number) + " created.")
	
	def processInterrupt(self):
		self.delta = time.time() - self.lasttime
		# if this is a start of pulse, then increment
		if GPIO.input(self.number) == False:
			self.counter += 1
			print("time.time() - lasttime:%s, counter%s" % \
				(time.time() - self.lasttime, self.counter))
		elif GPIO.input(self.number) == True:
			self.timer.cancel()
			self.initTimer()
			self.timer.start()
		#if self.delta > self.pulselength:
			#print("Total number of pulses:{}".format(self.counter))
			#self.counter = 0
		#self.lasttime = time.time()

	def initTimer(self):
		self.timer = Timer(self.pulselength + 0.1, self.playAudio)

	def playAudio(self):
		if(self.number == INPUT0):
			print("Warning!!!")
		else:
			print("Playing audio number " + str(self.number))
		
	
input0 = RInput(INPUT0, 2.5);

while True:
	time.sleep(1)
