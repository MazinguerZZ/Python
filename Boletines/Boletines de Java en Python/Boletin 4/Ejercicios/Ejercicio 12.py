# 12. Crear un programa que lea un número de año por teclado e indique si es bisiesto o
# no. Un año bisiesto es aquel que es divisible por 4, siempre y cuando no lo sea por
# 100. La excepción a esta regla son los años múltiplos de 400, que siempre son
# bisiestos.

anio = int(input("Dame el año: "))
if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
