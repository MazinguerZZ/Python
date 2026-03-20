# Modifica el programa anterior para que al iniciar el juego te pida dos parámetros con
# objeto de cambiar la dificultad del juego: el número máximo (antes era siempre 50) o
# el número de intentos posibles (antes era siempre 5).

import random

volver_jugar = False
contador = 0
contador2 = int(input("Numero maximo de intentos: "))
num_max = int(input("Nuevo numero maximo para aumentar dificultad: "))
num_aleatorio = random.randint(1, num_max)


while contador < contador2:

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