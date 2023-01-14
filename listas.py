lista = [20, 14, 3, 7, 0, 7, 41]
a = [101, 100, 140,113]

#lista.append("f")
#lista.pop(1)


lista_one = list(range(100))
#double = [i * 2 for i in lista_one]
pares = [i for i in lista_one if i %2 == 0]

"""lista.extend(range(5,20))""" 
lista.extend(a) #extiende la lista con valores dentro de un iterable como un range()

lista.insert(0, 7) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.

lista.pop() #Elimina valor en la posición i de la lista.

lista.remove(140) #Elimina el primer elemento con ese valor.

lista.index(20) #Retorna posición del primer elemento con el valor.
# lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)

lista.count(7) #Cuenta cuántas veces esta ese valor en la lista.

lista.sort() #Ordena los elementos de menor a mayor.

lista.sort(reverse = True) #Ordena los elementos de mayor a menor.

lista.reverse() #Invierte los elementos

nueva_lista = lista.copy() #Genera una copia de la lista. También útil para clonar listas.
nueva_lista.reverse() #Le da la vuelta a la lista actual

lista_text = list("Hola mundo")
lista_text.reverse()
cadena = "".join(lista_text)

#lista.clear() #Borra elementos en la lista.

print(cadena)