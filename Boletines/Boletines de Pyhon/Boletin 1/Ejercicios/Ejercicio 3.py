# 3. Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado
# por el usuario

num = int(input("Ingrese un numero: "))

for i in range(1, num + 1):
    print(i * num)