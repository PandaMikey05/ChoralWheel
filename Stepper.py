import RPi.GPIO as gpio
from time import sleep
from time import time
print("starting")
def setState(pinList, states):
    for i in range(0,len(pinList)):
        gpio.output(pinList[i],states[i])
gpio.setmode(gpio.BCM)
A1=22
gpio.setup(A1,gpio.OUT)
A2=27
gpio.setup(A2,gpio.OUT)
B1=17
gpio.setup(B1,gpio.OUT)
B2=24
gpio.setup(B2,gpio.OUT)
pins=[A1,B1,A2,B2] #CW pin configuration, reverse order for CCW
#pins=[A1,B2,A2,B1]
#pins=[A1,B2,A2,B1]
print("pins assigned")
steps=400
stepsPerRev=200
stepTime=0.1

on=gpio.HIGH
off=gpio.LOW

for i in range(0,200):
    setState(pins,[gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH])
    sleep(stepTime/8)
    setState(pins,[on,off,off,off])
    sleep(stepTime/8)
    
    setState(pins,[gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW])
    sleep(stepTime/8)
    setState(pins,[off,on,off,off])
    sleep(stepTime/8)
    
    setState(pins,[gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW])
    sleep(stepTime/8)
    setState(pins,[off,off,on,off])
    sleep(stepTime/8)
    
    setState(pins,[gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH])
    sleep(stepTime/8)
    setState(pins,[off,off,off,on])
    sleep(stepTime/8)

gpio.cleanup()
