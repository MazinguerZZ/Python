# 8. Modifica el programa anterior para que sea el usuario quién introduzca dos números y
# se nos muestre los primos que hay entre ambos

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

for i in range(numero1, numero2):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)