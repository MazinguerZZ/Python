# 1. Escribir un programa en python que nos pida tres números en cualquier orden y nos los
# muestre en pantalla ordenados de menor a mayor

num1 = int(input("Dame el primer número: "))
num2 = int(input("Dame el segundo número: "))
num3 = int(input("Dame el tercer número: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
medio = (num1 + num2 + num3) - mayor - menor

print(menor, "<", medio, "<", mayor)