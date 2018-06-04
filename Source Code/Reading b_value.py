import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
x = 1

while True:
    if(GPIO.input(7) == True):
        if(x==0):
            print('pin 7 HIGH')
            x = 1
    else:
        if(x==1):
            print('pin 7 LOW')
            x = 0
