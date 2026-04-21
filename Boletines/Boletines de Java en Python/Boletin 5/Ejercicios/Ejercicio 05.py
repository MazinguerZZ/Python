# 5. Escribe un programa que genere 100 números aleatorios comprendidos entre el 1 y
# 50 (ambos inclusive) y, posteriormente, obtenga el mayor, el menor y el que mas veces
# se repite (y nos diga cuantas veces lo hace).
import random

numeros = []
num_max_repetido = 0
repetido = 0

for i in range(100):
    num = random.randint(1, 50)
    numeros.append(num)

for i in range(1, 51):
    veces = numeros.count(i)
    if veces > num_max_repetido:
        num_max_repetido = veces
        repetido = i

max_num = max(numeros)
min_num = min(numeros)
print("El numero mayor es el: ", max_num)
print("El numero menor es el: ", min_num)
print("El número que mas veces se ha repetido ha sido el ", num_max_repetido, " y se ha repetido ",repetido, " veces.")
