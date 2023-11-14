from machine import Pin, PWM
import time

NS10 = 16

# creamos un Pulse Width Modulation Object en el siguiente pin
NS10= PWM(Pin(NS10),freq=440,duty=512)

def juno (freq, sleep):
    NS10.freq(freq)
    NS10.duty(512)
    time.sleep(sleep)
while True:
    juno(262,0.3)
    juno(293,0.3)
    juno(330,0.3)
    juno(349,0.3)
    juno(391,0.3)
    juno(440,0.3)
    juno(494,0.3)
    juno(523,0.3)