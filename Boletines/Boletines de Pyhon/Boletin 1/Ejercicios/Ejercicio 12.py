# 12. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando
# una primitiva). Por el momento no te preocupes de que algunos números puedan salir
# repetidos. Ya resolveremos eso más adelante.
import random

for i in range(1, 7):
    num_random = random.randint(1, 49)
    print(num_random, end=" ")