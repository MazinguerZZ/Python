# 1. Escribir un programa en python que pida al usuario un número y escriba todos sus
# divisores

numero = int(input("Introduce un número: "))
print(f"Los divisores de {numero} son: ")

for i in range(1, numero):
    if numero % i == 0:
        print(i)