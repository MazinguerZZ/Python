# Modifica el programa anterior para que el programa te de todos los intentos que
# necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
# lograrlo

import random

contador = 0
num_aleatorio = random.randint(1, 50)

while True:
    entrada = int(input("Ingrese un numero: "))
    contador += 1
    if entrada == num_aleatorio:
        print("Has acertado")
        print(f"Has fallado {contador} veces")
        break
    if entrada < num_aleatorio:
        print("El numero es mayor que el numero ingresado")
    elif entrada > num_aleatorio:
        print("El numero es menor que el numero ingresado")
