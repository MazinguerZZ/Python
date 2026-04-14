# 6. Modifica el ejercicio anterior para que, nos muestre en que posición del array se
# encuentran el máximo y el mínimo. Si están repetidos y aparecen en mas de una
# posición debería de indicarlas todas
import random

numero = int(input("Ingrese un numero: "))

lista = []

for i in range(numero):
    num_aleatorio = random.randint(10, 1000)
    lista.append(num_aleatorio)

maximo = max(lista)
minimo = min(lista)
media_aritmetica = sum(lista) / len(lista)

posicion_max = []
posicion_min = []

for j in range(len(lista)):
    if lista[j] == maximo:
        posicion_max.append(j)
    if lista[j] == minimo:
        posicion_min.append(j)

print("El mayor de la lista es el: ", maximo, " y esta en la posicion ",
      str(posicion_max).replace("[", "").replace("]", ""),
      ", el menor es el: ", minimo, " y esta en la posición ",
      str(posicion_min).replace("[", "").replace("]", ""),
      " y la media aritmetica es de: ", media_aritmetica)
