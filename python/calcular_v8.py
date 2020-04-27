import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

os.system('clear')

print('Universidad Tecnológica Israel'.center(80))
print('Ingeniería en Sistemas Informáticos'.center(80))
print('CP-Medidas de Física: Cinemática'.center(80))
print('Ismael Rodríguez T'.center(80))
print(' ')
print('Distancia:  1.2m')
print('Dos sensores LDR\n')

t=0
t1=0
t2=0

vi=0
vf=0
d=1.2
a=0

seguir = True

while seguir:
    if GPIO.input(23):
        time.sleep(0.1)
        t1 = time.time()
    if GPIO.input(24):
        time.sleep(0.1)
        t2 = time.time()
        t = t2-t1     
    if t > 0 and GPIO.input(24) == 0:
        seguir = False
        #vf = (((2*d)/t)-vi)
        #a = (((-2*vi)+((2*d)/t))/t)
        vf = (2*d)/t;
        a = ((2*d)/t)/t;
        print('Distancia:', d,'m')
        print('Tiempo:', round(t, 6),'s')
        print('Velocidad:', round (vf, 6),'m/s')
        print('Aceleracion:', round (a, 6),'m/s(2)')
GPIO.cleanup()
