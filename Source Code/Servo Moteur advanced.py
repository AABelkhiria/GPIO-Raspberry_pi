import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18,50)
pos = 0
p.start(pos)

try:
    while(1):
        for x in range(100):
            pos = pos + 1
            p.ChangeDutyCycle(pos)
            sleep(0.1)
        for x in range(100):
            pos = pos - 1
            p.ChangeDutyCycle(pos)
            sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
