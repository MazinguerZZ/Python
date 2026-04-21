# 16. Escribir un programa que genere un número aleatorio entre el 10.000.000 y el
# 50.000.000 que sea primo
import random

esPrimo = False
num_random = 0

while not esPrimo:
    num_random = random.randint(10000000, 50000000)
    esPrimo = True

    for i in range(2, num_random):
        if num_random % i == 0:
            esPrimo = False
            break
print(num_random, "es primo")