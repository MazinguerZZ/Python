# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# pida una palabra y diga cuántas veces aparece esa palabra en la lista.

num = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []

if num == 0:
    print("¡Imposible!")
else:
    for i in range (num):
        nombre = input(f"Dígame la palabra {i+1}: ")
        lista.append(nombre)
    print("La lista creada es: ", lista)

palabra = input("Dígame la palabra a buscar: ")
if palabra in lista:
    print(f"La palabra '{palabra}' aparece {lista.count(palabra)} veces en la lista.")
else:
    print(f"La palabra '{palabra}' no aparece en la lista.")