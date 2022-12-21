
# objetivo = int(input('digite un entero positivo: '))
# sqr = 0
# respuesta = sqr ** (1/2)

# while respuesta < objetivo:
#     sqr += 1

#     if (respuesta)%1 == 0.0:
#         print('Tiene raiz cuadrada')
#     else:
#         print('no tiene raiz cuadrada')


objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')

