# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la
# lista al revés, sino de crear una lista distinta).

num = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []

if num == 0:
    print("¡Imposible!")
else:
    for i in range (num):
        palabra = input(f"Dígame la palabra {i+1}: ")
        lista.append(palabra)
    print("La lista creada es: ", lista)

lista_inversa = lista[::-1]
print("La lista inversa es: ", lista_inversa)