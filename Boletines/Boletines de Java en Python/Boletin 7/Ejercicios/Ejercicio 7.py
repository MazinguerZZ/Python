# 7. Pide al usuario un número y crea un array de enteros de tantas posiciones como indique
# ese número. Rellénalo con números aleatorios entre el 10 y el 1000 y finalmente
# pregunta al usuario por la posición de la que quiere recuperar el valor. El programa
# mostrará el número de la posición indicada si esta existe y un error si tratamos de
# recuperar una posición que no existe (menor a 0 o mayor a la longitud del array)
import random

numero = int(input("Ingrese un numero: "))
posicion = int(input("Ingrese una posicion para recuperar: "))

lista = []

for i in range(numero):
    num_aleatorio = random.randint(10, 1000)
    lista.append(num_aleatorio)

if  0 <= posicion < len(lista):
    print(lista[posicion])
else:
    print("No puede estar por debajo de 0 ni mayor de ", numero)
