import RPi.GPIO as GPIO
from time import sleep

# For I600 RaspberyPi v2
red = 10  # GPIO number where red led is connected
green = 22 # GPIO number where green led is connected
blue = 27 # GPIO number where blue led is connected

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Reset led light
def cleanLed():
  GPIO.output(red, True)
  GPIO.output(blue, True)
  GPIO.output(green, True)

# turn on red led
def redOn():
  GPIO.output(red, False)

# turn on blue led
def blueOn():
  GPIO.output(blue, False)

# turn on green led
def greenOn():
  GPIO.output(green, False)
