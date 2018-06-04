import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18,50)
p.start(1)

while(1):
    pos = input('get a position (0.0 to 100.0) : ')
    if(pos < 0):
        print('Position can t be negatif')
        pos = 1
    elif(pos >100):
        print('Position can t be higher than 100')
        pos = 100
    p.ChangeDutyCycle(pos)
    print('Please wait until the Servo Motor Stops')
