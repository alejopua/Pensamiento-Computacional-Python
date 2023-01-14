"""El programa tiene la finalidad de calcular una raiz cuadrada lo mas aproximada posible, realizando multiples iteraciones"""
"""Solicita al usuario un int objetivo positivo"""

from time import time

objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0
tiempo_inicio = time()

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

tiempo_total = time() - tiempo_inicio

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada del objetivo')
    print(f'Tardo {tiempo_total} segundos')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    print(f'Tardo {tiempo_total} segundos')


