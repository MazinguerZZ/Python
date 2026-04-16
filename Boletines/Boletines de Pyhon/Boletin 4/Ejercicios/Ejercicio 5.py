# 5. Escribir un programa que pida números enteros por teclado. La ejecución terminará
# cuando el usuario introduzca la palabra EXIT. En ese momento debería de mostrar un
# mensaje diciendo el número de números introducidos, la suma de todos y su media
# aritmética.
import math

esExit = True
numeros = 0
contador = 0

while esExit:
    numero = str(input("Introduce un número entero: "))
    if numero == "EXIT":
        esExit = False
        print(f"Has introducido {contador} números.")
        print("La suma de todos da: ", numeros)
        print("La media aritmética es: ", math.sqrt(numeros))
    else:
        contador += 1
        numeros += int(numero)

