
objetivo = int(input('digite un entero positivo: '))
sqr = 0

while sqr < objetivo:
    sqr += 1
    respuesta = sqr ** (1/2)
    print(respuesta)


if (respuesta)%1 == 0.0:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}, es exacta.')
else:
    print(f'{objetivo} no tiene raiz cuadrada exacta.')
