# 6. Escribe un programa que nos permita contar el número de veces que se repite cada
# cifra en un número. Por ejemplo, el número 885210003 tiene tres 0, un 1, un 2, un 5 y
# dos 8.

num = input("Ingrese un numero: ")

contadores = [0,0,0,0,0,0,0,0,0,0]

for i in num:
    contadores[int(i)] += 1

for i in range(10):
    if contadores[i] > 0:
        print("El numero ", i , " se repite ", contadores[i], " veces.")