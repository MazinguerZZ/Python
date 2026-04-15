# 2. Queremos hacer un programa que reciba un número por teclado y nos calcule tantos
# números de la sucesión de fibonacci como indique ese número. Por ejemplo, si
# metemos un 8 la salida de tu programa debería de ser así:
# 0,1,1,2,3,5,8,13

num = int(input("Ingrese un numero: "))

a, b = 0, 1

for i in range(num):
    if i < num - 1:
        print(a, end=", ")
    else:
        print(a)
    a, b = b, a + b
