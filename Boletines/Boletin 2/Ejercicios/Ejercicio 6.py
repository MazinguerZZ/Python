# Modifica el ejercicio anterior para que la nota del boletín se redondee
# matemáticamente si es superior a 5 pero se trunquen los decimales si es inferior a 5

import math

nota1 =  float(input("Nota del trabajo en clase: "))
nota2 =  float(input("Nota de los ejercicios: "))
nota3 =  float(input("Nota del examen: "))

notafinal1 = (nota1 * 0.05) + (nota2 * 0.15) + (nota3 * 0.8)
notafinal2 = (nota1 * 0.05) + (nota2 * 0.15) + (nota3 * 0.8)

if notafinal1 and notafinal2 < 5:
    print("Nota redondeada: ", math.trunc(round(notafinal2, 2)))
    print("Nota sin redondear: ", round(notafinal1, 2))
else:
    print("Nota redondeada: ", int(round(notafinal2)))
    print("Nota sin redondear: ", round(notafinal1, 2))