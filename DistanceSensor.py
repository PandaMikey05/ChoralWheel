from time import sleep
from datetime import datetime
import RPi.GPIO as gpio
def DistanceSensorSetup():
    gpio.setmode(gpio.BCM)
    gpio.setup(13,gpio.OUT)
    gpio.setup(14,gpio.IN, pull_up_down=gpio.PUD_UP)
def GetCurrentDistance(speedOfSound=343):
    gpio.output(13,gpio.HIGH)
    sleep(0.00001)
    gpio.output(13,gpio.LOW)
    while(gpio.input(14)==gpio.LOW):
        a=1
    startingTime=datetime.now()
    while(gpio.input(14)==gpio.HIGH):
        a=2
    finalTime=(datetime.now()-startingTime).total_seconds()
    return speedOfSound*finalTime/2
