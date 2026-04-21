# 1. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
# ninguno de ellos esté repetido (simulando una lotería primitiva).
import random

primitiva = []
while len(primitiva) < 6:
    num = random.randint(1, 49)
    if num not in primitiva:
        primitiva.append(num)
print(primitiva)