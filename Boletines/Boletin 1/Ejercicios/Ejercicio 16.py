# Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando una
# lotería primitiva). Por el momento no te preocupes de que algunos números puedan salir
# repetidos. Ya resolveremos eso más adelante
import random

numero_loteria = random.sample(range(1, 49),6)

numeros = str(numero_loteria)
numeros = numeros.replace("[", " ")
numeros = numeros.replace("]", " ")

print(numeros)