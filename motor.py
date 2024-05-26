import RPi.GPIO as GPIO
import time

ena=18 #board pin 12
in1=14 #board pin 8
in2=15 #board pin 10
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ena, GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

pwm_frequency=5000 #in Hz
pwm_motor_1=GPIO.PWM(ena, pwm_frequency)
pwm_motor_1.start(50) #Duty cycle in percentage

def stop(speed):
    while speed>10:
        pwm_motor_1.ChangeDutyCycle(speed)
        speed=speed-10
        time.sleep(0.1)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    
def forward(speed):
    pwm_motor_1.ChangeDutyCycle(speed)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

def backward(speed):
    pwm_motor_1.ChangeDutyCycle(speed)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
speed=0
while True:
    c=input("Enter Choise:")
    if(c=='s'):
        stop(speed)
    elif(c=='f'):
        speed=int(input("enter speed:"))
        forward(speed)
    elif(c=='b'):
        speed=int(input("enter speed:"))
        backward(speed)
#GPIO.cleanup()

