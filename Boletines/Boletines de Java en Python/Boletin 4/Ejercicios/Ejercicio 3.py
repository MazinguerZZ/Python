# 3. Queremos ahora hacer un programa que reciba un número por teclado y nos muestre
# en orden todos los números de la sucesión de fibonacci que sean menores o iguales
# al que has enviado como argumento. Por ejemplo, si metemos el número 4 nos
# debería de devolver esto:
# 0,1,1,2,3

num = int(input("Ingrese un numero: "))

a, b = 0, 1
while a < num:
    if b > num or b == num:
        print(a)
    else:
        print(a, end=", ")
    a, b = b, a + b


