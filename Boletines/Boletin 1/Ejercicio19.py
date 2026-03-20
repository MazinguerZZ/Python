# Escribir un programa que pida un número por teclado y nos muestre sus divisores

numero = int(input("Dime un numero: "))

for divisor in range(1, numero - 1):
    if numero % divisor == 0:
        print(divisor)

