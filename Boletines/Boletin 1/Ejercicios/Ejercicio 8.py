# Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
# (puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
# número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
# intereses de ningún tipo y redondeamos a dos decimales.

numero = float(input("Cantidad de dinero a dar: "))
meses = int(input("Numero de meses: "))
print("Cantidad a pagar cada mes", round(float(numero / meses),2))