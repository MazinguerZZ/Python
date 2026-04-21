# 6. Escribir un programa que muestre por pantalla los 50 primeros números primos, sus
# raíces cuadradas, sus cuadrados y sus cubos

contador = 0
primo = 2
esPrimo = True

while contador < 50:

    for i in range(2, primo):
        if primo % i == 0:
            esPrimo = False

    if esPrimo:
        contador += 1
        print(primo)
    primo += 1
    esPrimo = True