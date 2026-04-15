# 1. Escribir un programa que pida un número por teclado y calcule su factorial. Como
# sabes, la factorial de un número se calcula multiplicando ese número por los
# sucesivos factores que obtenemos restando uno hasta llegar a la unidad

num = int(input("Ingrese un numero: "))
fatorial = 1
operacion = ""
for i in range(num, 0, -1):
    fatorial = fatorial * i
    operacion = operacion + str(i)

    if i > 1:
        operacion = operacion + "*"

print(num, "! =", operacion, "=", fatorial)
