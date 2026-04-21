# 10. Escribir un programa que nos pida dos números y genere un número aleatorio
# comprendido entre ambos. Por el momento no te preocupes de que el primer número
# siempre debería de ser menor que el segundo, simplemente no los metas en un orden
# incorrecto.
import random

numero1 = int(input("Dame un número: "))
numero2 = int(input("Dame otro número: "))

num_random = random.randint(numero1, numero2)
print(num_random)