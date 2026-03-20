# Escribir un programa que nos pida por teclado dos calificaciones numéricas de un
# alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las
# notas introducidas deben de estar entre 0 y 10 y admiten decimales. Caso de que una
# entrada sea errónea debería de advertirnos de ello y no hacer el cálculo

nota = float(input("Primera nota: "))
nota2 = float(input("Segunda nota: "))

if nota and nota2 < 10:
    nota_aritmetica = float(nota + nota2) / 2
    print("La nota final es: ", int(round(nota_aritmetica,0)))
else:
    print("La nota es mayor que 10")