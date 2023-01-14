diccionario = {
    'Diana' : 20,
    'Pedro' : 25,
    'Paula' : 30,
}

diccionario['Mona'] = 65

diccionario['Paula'] = 31

for llave in diccionario.keys():
    print(llave)

for valor in diccionario.values():
    print(valor)

for llave, valor in diccionario.items():
    print(llave, valor)

print(diccionario)
print(5/'platzi')
