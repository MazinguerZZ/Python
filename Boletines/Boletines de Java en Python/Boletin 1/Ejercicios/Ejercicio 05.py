# Escribir un programa que pida por teclado un número al usuario y diga si es par o impar
numero = int(input("Dame un numero: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")