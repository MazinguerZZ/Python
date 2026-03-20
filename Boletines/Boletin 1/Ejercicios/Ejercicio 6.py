# Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o no
numero = int(input("Dame un numero: "))
if numero % 3 == 0:
    print("El numero es divisible entre 3")
else:
    print("No es divisible entre 3")