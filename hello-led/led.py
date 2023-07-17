import RPi.GPIO as GPIO
from time import sleep

pin = 7
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)

while(True):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(3)
    GPIO.cleanup()

