# 6. Escribir un programa que pida un número al usuario y diga si es divisible por 3 o no.

numero = int(input("Ingrese un numero: "))

if numero % 3 == 0:
    print("El número es divisible por 3")
else:
    print("El número no es divisible por 3")