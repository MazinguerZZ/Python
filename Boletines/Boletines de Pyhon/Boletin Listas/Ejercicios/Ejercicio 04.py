# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# pida una palabra y elimine esa palabra de la lista.

num = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []

if num == 0:
    print("¡Imposible!")
else:
    for i in range (num):
        palabra = input(f"Dígame la palabra {i+1}: ")
        lista.append(palabra)
    print("La lista creada es: ", lista)

palabra_eliminar = input("Palabra a eliminar: ")
for palabra in lista:
    lista.remove(palabra_eliminar)
print("La lista esahora: ", lista)