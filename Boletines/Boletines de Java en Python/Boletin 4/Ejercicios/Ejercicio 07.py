# 7. Decimos que dos números primos son gemelos cuando están separados por un único
# número (el 11 y el 13, el 17 y el 19, el 41 y el 43, etc.). Escribir un programa que calcule
# la primera pareja de primos gemelos por encima del 50.

esPrimo1 = True
esPrimo2 = True
num = 51


while True:
    esPrimo1 = True
    for i in range(2, num):
        if num % i == 0:
            esPrimo1 = False

    esPrimo2 = True
    for i in range(2, num + 2):
        if (num + 2) % i == 0:
            esPrimo2 = False

    if esPrimo1 and esPrimo2:
        print("La pareja de primos son", num, "y", num + 2)
        break

    num += 1
