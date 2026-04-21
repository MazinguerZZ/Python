# 4. Escribir un programa donde se muestren todos los números divisibles por 7 menores a
# 10000

for i in range(1, 1000):
    if i % 7 == 0:
        print(i)