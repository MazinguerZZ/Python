# 6. Modificar el programa anterior para que, además, nos diga cual han sido el número
# mayor y el menor que has introducido
import math

esExit = True
numeros = 0
contador = 0
mayor = None
menor = None

while esExit:
    numero = str(input("Introduce un número entero: "))
    if numero == "EXIT":
        esExit = False
        print(f"Has introducido {contador} números.")
        print("La suma de todos da: ", numeros)

        if contador > 0:
            print("La media aritmética es: ", numeros / contador)
            print("El número mayor es el:", mayor)
            print("El número menor es el:", menor)
    else:
        numero = int(numero)

        contador += 1
        numeros += numero

        if mayor is None or numero > mayor:
            mayor = numero

        if menor is None or numero < menor:
            menor = numero