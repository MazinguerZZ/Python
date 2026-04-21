# Escriba un programa que permita crear dos listas de palabras y que, a continuación,
# elimine de la primera lista los nombres de la segunda lista.

num = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []

if num == 0:
    print("¡Imposible!")
else:
    for i in range (num):
        palabra = input(f"Dígame la palabra {i+1}: ")
        lista.append(palabra)
    print("La lista creada es: ", lista)

eliminar = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))
lista2 = []
for j in range (eliminar):
    palabra2 = input(f"Dígame la palabra {j+1}: ")
    lista2.append(palabra2)
print("La lista de palabras a eliminar es: ", lista2)
for palabra in lista2:
    while palabra in lista:
        lista.remove(palabra)

print("La lista es ahora: ", lista)


