# Escribir un programa que genere un número primo aleatorio entre el 10.000.000 y el
# 50.000.000
import random

es_primo = False
num = 0

while not es_primo:
    num = random.randint(10000000, 50000000)
    es_primo = True

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
print(num, "es primo")