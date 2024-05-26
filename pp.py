import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


for i in range(0,5):
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    
    time.sleep(0.5)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.5)


GPIO.cleanup()
