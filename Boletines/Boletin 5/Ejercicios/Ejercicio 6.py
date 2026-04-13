# 6. Escribe un programa que nos permita contar el número de veces que se repite cada
# cifra en un número. Por ejemplo, el número 885210003 tiene tres 0, un 1, un 2, un 5 y
# dos 8.

num = input("Ingrese un numero: ")

contador0 = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0
contador7 = 0
contador8 = 0
contador9 = 0

for i in num:
    if i == "0":
        contador0 += 1
    elif i == "1":
        contador1 += 1
    elif i == "2":
        contador2 += 1
    elif i == "3":
        contador3 += 1
    elif i == "4":
        contador4 += 1
    elif i == "5":
        contador5 += 1
    elif i == "6":
        contador6 += 1
    elif i == "7":
        contador7 += 1
    elif i == "8":
        contador8 += 1
    elif i == "9":
        contador9 += 1

print(contador0, contador1, contador2, contador3, contador4, contador5, contador6, contador7, contador8, contador9)
