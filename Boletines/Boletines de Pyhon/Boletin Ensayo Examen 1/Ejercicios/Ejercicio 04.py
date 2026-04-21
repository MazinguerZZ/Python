# Ejercicio 4 – RA3 (2 puntos)
# Rick Sánchez al fin ha revelado el secreto detrás de su pistola de portales
# interdimensionales y se te ha pedido crear una réplica.
# Para sorpresa de todos, funciona mediante un programa escrito en Python que
# genera un número primo aleatorio entre el 5.000.000 y el 20.000.000 y lo
# muestra por consola.
import random

esPrimo = False
num_random = 0

while not esPrimo:
    num_random = random.randint(5000000, 20000000)
    esPrimo = True

    for i in range(2, int(num_random**0.5) + 1):
        if num_random % i == 0:
            esPrimo = False
            break
print(num_random, "es primo")