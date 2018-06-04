import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while(1):
    GPIO.output(7,True)
    sleep(1)
    GPIO.output(7,False)
    sleep(1)
    
