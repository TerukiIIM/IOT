from machine import Pin, PWM
import utime
import time

leds = [PWM(Pin(18, mode = Pin.OUT)), PWM(Pin(17, mode = Pin.OUT)), PWM(Pin(16, mode = Pin.OUT))]

for i in leds :
    i.freq(1_000)
    i.duty_u16(0)

def setColor (house) :
    for i in range(len(house)):
        leds[i].duty_u16(house[i]*256)

house = {
    "Gryffindor" : [255,0,0],
    "Slytherin" : [0,255,0],
    "Ravenclaw" : [0,0,255],
    "Hufflepuff" : [255,255,0]
}
setColor(house["Slytherin"])
