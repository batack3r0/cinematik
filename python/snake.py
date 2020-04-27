import math
raiz = math.sqrt(81)
#print("El resultado es: ", raiz)

#constante -> gravedad
g = 9.91
hora = 3600
km = 1000

#variables

d = 4
t = 1.0
vi = 0.0
a = 0.0

#switch
#caso 1

vf = (((2*d)/t)-vi)
a = (((-2*vi)+((2*d)/t))/t)

#resultados

vf = round(vf,5)
a = round(a,5)

print (a)