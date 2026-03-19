lista = []
lista2 = list()
lista3 = [2,5,6.5,7,8,12,7,14,12,5,5]
lista4 = ["Jorge", "Pepe", "Ana"]
print(lista3)
# # lista5 = lista3 + lista4 Lo mismo que lo de abajo
# # lista3.extend(lista4) # Lo mismo que lo de arriba
# lista3.append(14) # Añade al final de la lista
# print(lista3)
# lista3.insert(2, 15) # Mete el elemento 15 antes del elemento 2, siendo el primero el 0, y si pones el  index en negativo, empieza por el final
# print(lista3)
# print(lista3.count(5)) # Sirve para contar el numero de veces que aparece un numero en una lista
# print(lista3.index(5)) # Sirve para que te devuelva la primera posicion de donde esta el elemneto introducido

# texto = str(lista3)
# print(texto)
# texto = texto.replace("[", "") # Sustituye elementos
# texto = texto.replace("]", "")
# print(texto)
# texto2 = "Hola Mundo"
# lista5 = list(texto2) # Convierte a lista
# print(lista5)
#
# matriz = [[1,2,3], [4,5,6], [7,8,9]] # Hacer matriz
# print(matriz[1][0]) # Fila 1, columna 0 y devuelve 4
#
# print(lista3[:5]) # Obtengo una lista hasta la posicion 5, la 5 no incluida
# print(lista3[2:5]) # Obtengo una lista desde la posicion 2 hasta la posicion 5, la 5 no incluida
# print(lista3[5:]) # Obtengo una lista desde la posicion 5 hasta el final de la lista
# print(lista3[5::2]) # Obtengo una lista desde la posicion 5, saltando de 2 en 2
# print(lista3[5::-2]) # Obtengo una lista desde la posicion 5 hasta la -2 empezando por el final
# print(lista3[::-1]) # Le da la vuelta a la lista

if 4 in lista3:
    print("Esta en la lista")

if 4 not in lista3:
    print("No esta en la lista")


# Prueba Lamba
texto = lambda a,b:a+b
print(texto(5, 2))