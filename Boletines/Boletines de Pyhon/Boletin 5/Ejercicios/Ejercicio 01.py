# 1. Escribir un programa que genere una lista con 10 números aleatorios comprendidos
# entre el 1 y el 500 y la muestre por pantalla ordenada. A continuación nos debería de
# pedir un número por teclado y decirnos si está o no en la lista y cuantos de los números
# son menores al que le hemos dado
import random

lista = []

for i in range(1,11):
    numero_aleatorio = random.randint(1, 500)
    lista.append(numero_aleatorio)
print(sorted(lista))

numero = int(input("Introduce un número: "))
menores = 0
esta = False

for i in lista:
    if i == numero:
        esta = True

    if i < numero:
        menores += 1

if esta:
    print("El número esta en la lista.")
else:
    print("El número no esta en la lista.")

print("Cantidad de números menores:", menores)


