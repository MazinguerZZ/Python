# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

num = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []

if num == 0:
    print("¡Imposible!")
else:
    for i in range (num):
        palabra = input(f"Dígame la palabra {i+1}: ")
        lista.append(palabra)
    print("La lista creada es: ", lista)

lista_sin_repeticiones = list(set(lista))
print("La lista sin repeticiones es: ", lista_sin_repeticiones)