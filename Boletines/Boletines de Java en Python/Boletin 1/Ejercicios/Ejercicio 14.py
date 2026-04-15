# Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
# comprendido entre ambos. Por el momento no te preocupes de que el primer número
# siempre debería de ser menor que el segundo, simplemente no los metas en un orden
# incorrecto.
import random

numero = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))

print("Numero aleatorio:", random.randint(numero, numero2))