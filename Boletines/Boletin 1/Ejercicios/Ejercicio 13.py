# Modifica el programa anterior para que no admita dados con un número de caras impares
# (¡no existen!). En el caso de meter un número impar de caras el programa debería de
# informarnos de que es erróneo y volver a preguntarnos por este dato.

import random

tiradas = int(input("Numero de tiradas: "))
dados = tiradas
caras = int(input("Numero de caras (No valen impares): "))

while True:
    if caras % 2 != 0:
        print("No existen dados con numero de caras impares")
        caras = int(input("Numero de caras (No valen impares): "))
    else:
        for i in range(dados):
            dado = random.randint(0,caras)
            print(dado)
        break