import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, en, in1, in2):
        self.en = en
        self.in1 = in1
        self.in2 = in2
        self.speed = 0
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        
        self.pwm_frequency = 5000 # in Hz
        self.pwm_motor = GPIO.PWM(self.en, self.pwm_frequency)
        self.pwm_motor.start(0) # Duty cycle in percentage

    def stop(self):
        #while self.speed > 10:
        #    self.pwm_motor.ChangeDutyCycle(self.speed)
        #    self.speed -= 10
        #    time.sleep(0.1)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
    
    def forward(self, speed):
        self.speed=speed
        self.pwm_motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def backward(self, speed):
        self.speed=speed
        self.pwm_motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
