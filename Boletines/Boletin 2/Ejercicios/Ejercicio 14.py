# Modifica el programa anterior para que al final del programa te pida si quieres volver
# a jugar y en caso afirmativo comience una nueva partida

import random

contador = 0
num_aleatorio = random.randint(1, 50)
volver_jugar = False

while True:
    entrada = int(input("Ingrese un numero: "))
    contador += 1
    if entrada == num_aleatorio:
        print("Has acertado")
        print(f"Has fallado {contador} veces")
        entrada2 = input("Quieres volver a jugar? Si o No: ")
        if entrada2.lower() == "si":
            contador = 0
            num_aleatorio = random.randint(1, 50)
            volver_jugar = True
        else:
            break
    elif entrada < num_aleatorio:
        print("El numero es mayor que el numero ingresado")
    else:
        print("El numero es menor que el numero ingresado")