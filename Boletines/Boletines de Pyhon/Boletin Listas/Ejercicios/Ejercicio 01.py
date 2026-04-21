# Escriba un programa que permita crear una lista de palabras. Para ello, el programa
# tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
# Por último, el programa tiene que escribir la lista.

num = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []

if num == 0:
    print("¡Imposible!")
else:
    for i in range (num):
        palabra = input(f"Dígame la palabra {i+1}: ")
        lista.append(palabra)
    print("La lista creada es: ", lista)

