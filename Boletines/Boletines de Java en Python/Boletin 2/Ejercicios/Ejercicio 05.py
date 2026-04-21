# Escribir un programa que nos pida las notas obtenidas en un trimestre y nos muestre
# la media ponderada sabiendo que;
#  1. La primera nota corresponde al trabajo en clase y cuenta como un 5% del total
#  2. La segunda corresponde a los ejercicios prácticos: 15%
#  3. La tercera la nota del examen: 80%
#  El resultado debería de mostrarse de dos formas: redondeado con dos decimales
# (nota real) y sin redpmdeada sin decimales (nota de boletín).
nota1 =  float(input("Nota del trabajo en clase: "))
nota2 =  float(input("Nota de los ejercicios: "))
nota3 =  float(input("Nota del examen: "))

notafinal1 = (nota1 * 0.05) + (nota2 * 0.15) + (nota3 * 0.8)
notafinal2 = (nota1 * 0.05) + (nota2 * 0.15) + (nota3 * 0.8)

print("Nota redondeada: " ,round(notafinal1, 2))
print("Nota sin redondear: ", int(notafinal2))