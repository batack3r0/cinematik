import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

Encendido_1 = 23
Encendido_2 = 24

Apagado_1 = not GPIO.input(23)
Apagado_2 = not GPIO.input(24)

os.system('clear')

print('Universidad Tecnológica Israel'.center(80))
print('Ingeniería en Sistemas Informáticos'.center(80))
print('CP-Medidas de Física: Cinemática'.center(80))
print('Ismael Rodríguez T'.center(80))
print(' ')
print('Distancia:  1.2m')
print('Dos sensores LDR\n')

t=0.0
t1=0.0
t2=0.0

v=0.0
s=1.2
a=0.0

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
        v = s/t
        a = v/t
        print('Tiempo: ', round(t, 7),' s')
        print('Velocidad: ', round (v, 7), 'm/s')
        print('Aceleracion: ', round (a, 7), 'm/s(2)')
GPIO.cleanup()
