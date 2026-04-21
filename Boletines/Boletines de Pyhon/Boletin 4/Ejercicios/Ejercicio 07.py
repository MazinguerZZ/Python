# 7. Escribir un programa en Python que te escriba todos los números primos que hay entre
# el 1 y el 100

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)



