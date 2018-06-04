import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)


nb_blink = input('Get number of blinks : ')
tm_on = input('time on in seconds : ')
tm_off = input('time off in seconds : ')

input('\n Press Enter to Start !')
for x in range(nb_blink):
    GPIO.output(7,True)
    sleep(tm_on)
    GPIO.output(7,False)
    sleep(tm_off)
    
