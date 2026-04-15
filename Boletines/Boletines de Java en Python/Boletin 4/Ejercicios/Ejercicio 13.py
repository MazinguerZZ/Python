# 13. Hacer un programa que lea un número y un carácter y visualice una matriz compacta
# repitiendo ese carácter y con tantas filas y columnas como indique el número. Por
# ejemplo, si metemos el 4 y la x nos debería de mostrar esto:
# xxxx
# xxxx
# xxxx
# xxxx

num = int(input("Ingrese un numero: "))
caracter = input("Ingrese un caracter: ")

for i in range(num):
    for j in range(num):
        print(caracter, end=" ")
    print()