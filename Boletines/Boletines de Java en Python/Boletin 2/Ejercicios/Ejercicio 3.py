# Escribir un programa que pida un número por teclado al usuario que simule ser el
# precio de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado
# debe de estar redondeado a dos decimales

numero = float(input("Dame un numero: "))

print(round(numero*1.21, 2))
