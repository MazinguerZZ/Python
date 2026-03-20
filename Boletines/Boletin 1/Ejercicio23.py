# Escribir un programa que te escriba todos los números primos que hay entre el 1 y el 100

for num in range(2, 101):
    if num <= 1:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

