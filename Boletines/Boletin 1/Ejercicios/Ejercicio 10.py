#  Escribir un programa que genere dos números aleatorios simultáneamente entre el 1 y el 6
# (simulando una tirada de dos dados)
import random
dado1 = 1
dado2 = 6

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
print(dado1,"-", dado2)