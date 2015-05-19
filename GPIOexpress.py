#!/usr/bin/env/ python
                                                      
# Title  :  GPIO Express
# Author :  Ronan Casey
# Ver    :  1.00

import RPi.GPIO as GPIO
import time

# colors and pins dictionary
pins = { "blue" : 8, "red" : 10, "green" : 12 }        

# use pin numbers on the pi as reference
def setOutputs(): 
    GPIO.setmode(GPIO.BOARD)
    for key in pins:
        GPIO.setup(pins.get(key),GPIO.OUT) 

# turn off all pins
def turnAllOff():
    for key in pins:
        GPIO.output(pins.get(key),0)  
   
# clean up operation to close pins after use
def cleanUp():
    GPIO.cleanup()

# user enters color, duration and number of times
def turnOn(color, duration, times):
    pin = color.strip().lower()
    
    # key validtion
    if pin in pins:
        setOutputs()
        turnAllOff()
        
        # repeat according to parameter 'times'
        for i in range(int(times)):
            GPIO.output(pins.get(pin), 1)  # turn ON
            time.sleep(float(duration))    # delay set by 'duration'
            GPIO.output(pins.get(pin), 0)  # turn OFF
            time.sleep(float(duration))    # delay OFF equals delay ON above
        
        # always run the cleanup operation
        cleanUp()

