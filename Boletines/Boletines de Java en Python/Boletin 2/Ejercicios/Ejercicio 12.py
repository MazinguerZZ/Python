# Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
# ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
# has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
# se superan el número máximo de intentos establecidos en 5.

import random

contador = 0
num_aleatorio = random.randint(1, 50)

while contador < 5:
    entrada = int(input("Ingrese un numero: "))
    contador += 1
    if entrada == num_aleatorio:
        print("Has acertado")
        break
    if entrada < num_aleatorio:
        print("El numero es mayor que el numero ingresado")
    elif entrada > num_aleatorio:
        print("El numero es menor que el numero ingresado")


