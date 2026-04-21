# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# pida dos palabras y sustituya la primera por la segunda en la lista.

num = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []

if num == 0:
    print("¡Imposible!")
else:
    for i in range (num):
        palabra = input(f"Dígame la palabra {i+1}: ")
        lista.append(palabra)
    print("La lista creada es: ", lista)


sustituir = input("Sustituir la palabra: ")
insertar = input("por la palabra: ")
for palabra in lista:
    if palabra == sustituir:
        lista.remove(sustituir)
        lista.append(insertar)
print("La lista es ahora:", lista)