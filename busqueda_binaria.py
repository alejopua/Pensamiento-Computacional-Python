"""El calcula la raiz cuadrada de forma agil aplicando el concepto de busqueda binarias"""
"""Solicita al usuario un int objetivo positivo"""

from time import time

objetivo = int(input('Digita un numero entero positivo: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2
tiempo_inicio = time()

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta} ')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2

tiempo_total = time() - tiempo_inicio

print(f'La raiz cuadrada de {objetivo} es la {respuesta}')
print(f'Tardo {tiempo_total} segundos')
   