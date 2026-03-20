# Modifica el programa anterior para que sea el usuario quién introduzca dos números y se nos
# muestre los primos que hay entre ambos

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

for num in range(num1, num2):
    if num <= 1:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)