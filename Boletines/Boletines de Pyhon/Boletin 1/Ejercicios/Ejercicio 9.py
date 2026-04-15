# 9. Escribir un programa que genere dos números aleatorios simultáneamente entre el 1 y el
# 6 (simulando una tirada de dos dados)
import random

num_random1 = random.randint(1, 6)
num_random2 = random.randint(1, 6)

print(num_random1, "-", num_random2)