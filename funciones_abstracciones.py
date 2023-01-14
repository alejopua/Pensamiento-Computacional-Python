from time import time

"""El siguiente programa calcula raiz cuadrada con diversos metodos, tiene la opcion de elegirlos"""
"""1. Debe elegir el metodo a usar."""
"""2. Digitar el numero entero positivo del cual quiere calcular su raiz"""

def Exhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1
        print(respuesta)

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}.')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta.')

def Aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    tiempo_inicio = time()

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    tiempo_total = time() - tiempo_inicio

    if abs(respuesta**2 - objetivo) >= epsilon:
        print('No se encontro la raiz cuadrada del objetivo')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    print(f'Tardo {tiempo_total} segundos')

def Binaria(objetivo):
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

opcion = int(input("Digita el metodo a usar: \n 1. Enumeracion exhaustiva. \n 2. Aproximacion de soluciones. \n 3. Busqueda binaria. \n --> "))

if opcion == 1:
    print('Enumeriacion exhaustiva')
    objetivo = int(input('Digite un numero entero positivo: '))
    Exhaustiva(objetivo)
elif opcion == 2:
    print('Aproximacion de soluciones')
    objetivo = int(input('Digite un numero entero positivo: '))
    Aproximacion(objetivo)
elif opcion == 3:
    print('Busqueda binaria')
    objetivo = int(input('Digite un numero entero positivo: '))
    Binaria(objetivo)


