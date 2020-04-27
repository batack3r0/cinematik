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

tiempo = 0
seguir = True

while seguir:
    if GPIO.input(23):
        time.sleep(0.1)
        t1 = time.time()
    if GPIO.input(24):
        time.sleep(0.1)
        t2 = time.time()
        tiempo = t2-t1     
    if tiempo > 0 and GPIO.input(24) == 0:
        seguir = False
        t = (round (tiempo,6))
        print(t)
GPIO.cleanup()