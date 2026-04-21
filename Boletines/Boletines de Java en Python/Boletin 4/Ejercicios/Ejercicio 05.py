# 5. Escribir un programa que nos diga si un número es capicúa.

num = input("Ingrese un numero: ")

numero_invertido = num[::-1]

if num == numero_invertido:
    print("El numero es capicua")
else:
    print("El numero no es capicua")