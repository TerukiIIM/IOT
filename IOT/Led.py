from machine import Pin, PWM
import utime
import time	

pinNumber = [2, 6, 10, 14]

pin_button = Pin(17, mode=Pin.IN, pull=Pin.PULL_UP)

n = 0
switch = True

while True :
    if switch == True :
        for i in pinNumber :
            for j in range (10):
                n += 5000
                PWM(Pin(i,mode=Pin.OUT))
                PWM(Pin(i,mode=Pin.OUT)).freq(1_000)
                PWM(Pin(i,mode=Pin.OUT)).duty_u16(n)
                utime.sleep(0.1)

            for k in range (10):
                n -= 5000
                PWM(Pin(i,mode=Pin.OUT))
                PWM(Pin(i,mode=Pin.OUT)).freq(1_000)
                PWM(Pin(i,mode=Pin.OUT)).duty_u16(n)
                utime.sleep(0.1)
    else :
        for j in range (10):
            n += 5000
            PWM(Pin(pinNumber[0],mode=Pin.OUT))
            PWM(Pin(pinNumber[0],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[0],mode=Pin.OUT)).duty_u16(n)
            
            PWM(Pin(pinNumber[1],mode=Pin.OUT))
            PWM(Pin(pinNumber[1],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[1],mode=Pin.OUT)).duty_u16(n)
            
            PWM(Pin(pinNumber[2],mode=Pin.OUT))
            PWM(Pin(pinNumber[2],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[2],mode=Pin.OUT)).duty_u16(n)
            
            PWM(Pin(pinNumber[3],mode=Pin.OUT))
            PWM(Pin(pinNumber[3],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[3],mode=Pin.OUT)).duty_u16(n)
            utime.sleep(0.1)

        for k in range (10):
            n -= 5000
            PWM(Pin(pinNumber[0],mode=Pin.OUT))
            PWM(Pin(pinNumber[0],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[0],mode=Pin.OUT)).duty_u16(n)
            
            PWM(Pin(pinNumber[1],mode=Pin.OUT))
            PWM(Pin(pinNumber[1],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[1],mode=Pin.OUT)).duty_u16(n)
            
            PWM(Pin(pinNumber[2],mode=Pin.OUT))
            PWM(Pin(pinNumber[2],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[2],mode=Pin.OUT)).duty_u16(n)
            
            PWM(Pin(pinNumber[3],mode=Pin.OUT))
            PWM(Pin(pinNumber[3],mode=Pin.OUT)).freq(1_000)
            PWM(Pin(pinNumber[3],mode=Pin.OUT)).duty_u16(n)
            utime.sleep(0.1)
            
    if pin_button.value() == 0 :
        if switch == True :
            switch = False
        else :
            switch = True