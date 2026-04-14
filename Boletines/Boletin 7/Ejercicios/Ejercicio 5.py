# 5. Pide al usuario un número y crea un array de enteros de tantas posiciones como indique
# ese número. Rellenalo con números aleatorios entre el 10 y el 1000 y finalmente
# muestra cual es el máximo, cual el mínimo y la media aritmética con dos decimales.
import random

numero = int(input("Ingrese un numero: "))

lista = []

for i in range(numero):
    num_aleatorio = random.randint(10, 1000)
    lista.append(num_aleatorio)

maximo = max(lista)
minimo = min(lista)
media_aritmetica = sum(lista) / len(lista)
print("El mayor de la lista es el: ", maximo, ", el menor es el: ", minimo,
      " y la media aritmetica es de: ", media_aritmetica)