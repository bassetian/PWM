from machine import Pin, PWM
import time

NS10 = 16
C= 39
# creamos un Pulse Width Modulation Object en el pin seleccionado
NS10= PWM(Pin(NS10),freq=4000000,duty=512)
C=Pin(C,Pin.IN, Pin.PULL_UP)
def juno (freq, sleep):
    NS10.freq(freq)
    NS10.duty(512)
    time.sleep(sleep)

while(True):
    if C.value()==0:
        juno(262,0.1)
    else:
        NS10.duty(0)