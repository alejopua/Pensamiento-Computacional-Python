# Este programa compara las edades de dos usuarios.
# y menciona quien es mayor y por cuantos años.
# Pregunta nombre y edad.

def cal_edad(nombre_user1, nombre_user2, edad_user1, edad_user2):
    if edad_user1 > edad_user2:
        print(f'{nombre_user1} Es mayor que {nombre_user2} por {edad_user1 - edad_user2} años')
    elif edad_user1 < edad_user2:
        print(f'{nombre_user2} Es mayor que {nombre_user1} por {edad_user2 - edad_user1} años')
    else:
        print(f'{nombre_user1} y {nombre_user2} tienen la misma edad')

def reg_data():
    nombre_user1 = input('Usuario 1, digita tu nombre: ')
    edad_user1 = int(input('Digita tu edad: '))

    nombre_user2 = input('Usuario 2, digita tu nombre: ')
    edad_user2 = int(input('Digita tu edad: '))

    print(cal_edad(nombre_user1, nombre_user2, edad_user1, edad_user2))

if __name__ == "__main__":
    reg_data()