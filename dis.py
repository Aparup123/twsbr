import RPi.GPIO as apa
import time
apa.setwarnings(False)
led=17
trig = 23
echo = 24

apa.setmode(apa.BCM)
apa.setup(trig,apa.OUT)
apa.setup(echo,apa.IN)
apa.setup(led, apa.OUT)

def dist():
    apa.output(trig,True)
    time.sleep(0.0001)
    apa.output(trig,False)
    
    while apa.input(echo) == False :
    	start = time.time()
    while apa.input(echo) == True :
    	end = time.time()
    finaltime  = end - start
    distance = finaltime/0.000058
    print(distance)
    return distance 

while True:
    measuredDistance=dist()
    if measuredDistance<=10:
        apa.output(led, apa.HIGH)
    else:
        apa.output(led, apa.LOW)
    time.sleep(0.3)
apa.cleanup()
