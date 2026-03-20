# Modificar el programa del punto anterior para que si el primer número que metemos es
# mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el 50 y
# en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y no entre el
# 50 y el 10 que no tiene mucha lógica…)
import random

numero = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))

if numero > numero2:
    print("Numero aleatorio:", random.randint(numero2, numero))
else:
    print("Numero aleatorio:", random.randint(numero, numero2))
