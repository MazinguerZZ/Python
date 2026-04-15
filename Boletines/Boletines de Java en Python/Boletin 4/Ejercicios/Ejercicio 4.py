# 4. Escribir un programa que cuente el número de cifras que tiene un número (por
# ejemplo, el 8 tiene una cifra, el 221 tres y el 456789 seis).

num = int(input("Ingrese un numero: "))
contador = 1

while num // 10 != 0:
    contador += 1
    num = num // 10


print(contador)