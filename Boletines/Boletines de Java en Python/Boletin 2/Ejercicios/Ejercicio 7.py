# Escribir un programa que pida un número por teclado y nos imprima la tabla de
# multiplicar de dicho número del 1 al 10.

numero = int(input("Ingrese un numero: "))

for i in range(1, 11):
    print(numero, "X", i, "=", numero * i)