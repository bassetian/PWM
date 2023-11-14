from machine import Pin, PWM
import time

NS10 = 16
F=39
E=37
D=35
C=33
t=0.05
# creamos un Pulse Width Modulation Object en el pin seleccionado
NS10= PWM(Pin(NS10),freq=40,duty=512)
time.sleep(2)
NS10.duty(0)
F=Pin(F,Pin.IN, Pin.PULL_UP)
E=Pin(E,Pin.IN, Pin.PULL_UP)
D=Pin(D,Pin.IN, Pin.PULL_UP)
C=Pin(C,Pin.IN, Pin.PULL_UP)
def juno (freq, sleep):
    NS10.freq(freq)
    NS10.duty(512)
    time.sleep(sleep)

while(True):
    if F.value()==0:
        juno(349,t)
    elif E.value()==0:
        juno(329,t)
    elif D.value()==0:
        juno(293,t)
    elif C.value()==0:
        juno(261,t)
    else:
        NS10.duty(0)
