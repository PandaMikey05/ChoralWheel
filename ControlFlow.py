import DistanceSensor
import asyncio
import gpiozero
import pydub as pd
#import simpleaudio as siau
import threading
import RPi.GPIO as gpio
from datetime import datetime
from time import sleep
from time import time

gpio.setmode(gpio.BCM)

recordingLEDPin="GPIO21"
recordingButtonPin="GPIO26"
reverseLEDPin="GPIO5"
reverseButtonPin="GPIO18"
LeftPinDefault=[22,17,27,24]
LeftPinArray=[22,17,27,24]
#RightPinArray=
RightWheelTimeCoeff=0.1
startingTime=datetime.now()
playback=None
fileName="test.mp3"

print("initial conditions set")
for i in LeftPinArray:
    gpio.setup(i,gpio.OUT)


reverse=False
LeftSteps=[0,0]
RightSteps=[0,0]
stepsPerRev=200
reverseButton=gpiozero.Button(reverseButtonPin)
reverseLED=gpiozero.LED(reverseLEDPin)

def reversalRoutine():
    global reverse
    if not reverse:
        reverse=True
        reverseLED.on()
        LeftPinArray[0]=LeftPinDefault[2]
        LeftPinArray[1]=LeftPinDefault[3]
        LeftPinArray[2]=LeftPinDefault[0]
        LeftPinArray[3]=LeftPinDefault[1]
        LeftPinArray.reverse()
    else:
        reverse=False
        reverseLED.off()
        LeftPinArray[0]=LeftPinDefault[0]
        LeftPinArray[1]=LeftPinDefault[1]
        LeftPinArray[2]=LeftPinDefault[2]
        LeftPinArray[3]=LeftPinDefault[3]
        #LeftPinArray.reverse()
reverseButton.when_pressed=reversalRoutine
def on (pin):
    gpio.output(pin,gpio.HIGH)
    
def off (pin):
    gpio.output(pin,gpio.LOW)
def sequence():
    startingTime=datetime.now()
    start=startingTime
    #mp3=pd.AudioSegment.from_file("test.mp3",format="mp3")-20
    #playback=siau.play_buffer(mp3.raw_data,num_channels=mp3.channels,bytes_per_sample=mp3.sample_width,sample_rate=mp3.frame_rate)


    
    while True:
        currentTime=(datetime.now()-startingTime).total_seconds()
        if (currentTime>=10):
            #playback.stop()
            return
        on(LeftPinArray[0])
        off(LeftPinArray[1])
        off(LeftPinArray[2])
        on(LeftPinArray[3])
        sleep(0.01)
        on(LeftPinArray[0])
        on(LeftPinArray[1])
        off(LeftPinArray[2])
        off(LeftPinArray[3])
        sleep(0.01)
        off(LeftPinArray[0])
        on(LeftPinArray[1])
        on(LeftPinArray[2])
        off(LeftPinArray[3])
        sleep(0.01)
        off(LeftPinArray[0])
        off(LeftPinArray[1])
        on(LeftPinArray[2])
        on(LeftPinArray[3])
#        if False: #function to reverse playback
#            elapsed = (datetime.now()-start).total_seconds()
#            mp32=mp3[elapsed*1000:]+mp3[0:elapsed*1000]
#            mp3=mp32.reverse()
#            playback.stop()
#            playback=siau.play_buffer(mp32.raw_data,num_channels=mp3.channels,bytes_per_sample=mp3.sample_width,sample_rate=mp3.frame_rate)
#            start=datetime.now()
#        if False: #function to record audio
#            playback.stop()
#            
#            while False:
DistanceSensor.DistanceSensorSetup()
print("starting standby")
while True:
    if (DistanceSensor.GetCurrentDistance()<0.5):
        print("user found")
        sequence()
