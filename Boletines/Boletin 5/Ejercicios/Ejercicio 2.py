# 2. Hacer un programa en que nos permita calcular todos los
# divisores comunes a dos números

num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

divisores_comunes = []

limite = min(num,num2)

for i in range(1, limite + 1):
    if num % i == 0 and num2 % i == 0:
        divisores_comunes.append(i)
print("Divisores comunes: ", divisores_comunes)