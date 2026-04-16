# 4. Modifica el programa anterior para que el programa te de todos los intentos que
# necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
# lograrlo

import random

max_num = 50
contador = 0
hasAcertado = True
num_random = random.randint(1, max_num)

while hasAcertado:
    numero = int(input("Ingrese un número: "))
    if num_random < numero:
        print("El número es menor.")
        contador += 1
    elif num_random > numero:
        print("El número es mayor.")
        contador += 1
    elif num_random == numero:
        print("Has acertado.")
        print(f"Has fallado {contador} veces.")
        hasAcertado = False