# 11. Modificar el programa del punto anterior para que si el primer número que metemos es
# mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el
# 50 y en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y
# no entre el 50 y el 10 que no tiene mucha lógica...)
import random

numero1 = int(input("Dame un número: "))
numero2 = int(input("Dame otro número: "))

num_min = min(numero1, numero2)
num_max = max(numero1, numero2)

num_random = random.randint(num_min, num_max)
print(num_random)